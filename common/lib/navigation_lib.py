"""Navigation helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import runtime_state

__version__ = "2.0.0"


def start_navigation(map_name: str | None = None):
    state = runtime_state()
    state.nav_active = True
    state.nav_map_name = map_name or state.slam_map_name
    return status()


def set_pose(x: float, y: float, yaw_deg: float):
    state = runtime_state()
    state.pose_x = float(x)
    state.pose_y = float(y)
    state.yaw_deg = float(yaw_deg)
    return {"x": state.pose_x, "y": state.pose_y, "yaw_deg": state.yaw_deg}


def go_to(x: float, y: float, yaw_deg: float = 0.0):
    state = runtime_state()
    state.nav_goal = (float(x), float(y), float(yaw_deg))
    state.nav_active = True
    return {"goal": state.nav_goal, "map_name": state.nav_map_name}


def cancel_goal():
    runtime_state().nav_goal = None
    runtime_state().nav_waypoints = []
    return status()


def is_busy():
    return runtime_state().nav_goal is not None or bool(runtime_state().nav_waypoints)


def wait_until_arrived(timeout_s: float | None = None):
    state = runtime_state()
    if state.nav_goal is not None:
        x, y, yaw_deg = state.nav_goal
        set_pose(x, y, yaw_deg)
        state.nav_goal = None
    while state.nav_waypoints:
        x, y, yaw_deg = state.nav_waypoints.pop(0)
        set_pose(x, y, yaw_deg)
    return {"arrived": True, "timeout_s": timeout_s, "pose": set_pose(runtime_state().pose_x, runtime_state().pose_y, runtime_state().yaw_deg)}


def waypoints(points: list[tuple[float, float, float]]):
    runtime_state().nav_waypoints = [(float(x), float(y), float(yaw_deg)) for x, y, yaw_deg in points]
    return {"queued": len(runtime_state().nav_waypoints)}


def status() -> dict:
    state = runtime_state()
    return {
        "nav_active": state.nav_active,
        "map_name": state.nav_map_name,
        "goal": state.nav_goal,
        "waypoints": list(state.nav_waypoints),
    }
