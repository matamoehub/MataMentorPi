"""Real navigation helpers backed by MentorPi navigation and navigation_controller."""

from __future__ import annotations

import time

from _mentorpi_ros import call_service, publish, start_launch, wait_for_message

__version__ = "3.0.0"


def start_navigation(map_name: str | None = None):
    args = {"map": map_name or "map_01"} if map_name else None
    nav_pid = start_launch("mentorpi_navigation", "navigation", "navigation.launch.py", launch_args=args)
    ctrl_pid = start_launch("mentorpi_navigation_controller", "large_models", "vllm_navigation.launch.py")
    return {"navigation_pid": nav_pid, "controller_pid": ctrl_pid, "map_name": map_name or "map_01"}


def set_pose(x: float, y: float, yaw_deg: float):
    result = call_service(
        "navigation_controller/set_pose",
        "interfaces.srv",
        "SetPose2D",
        lambda req: (
            setattr(req.data, "x", float(x)),
            setattr(req.data, "y", float(y)),
            setattr(req.data, "roll", 0.0),
            setattr(req.data, "pitch", 0.0),
            setattr(req.data, "yaw", float(yaw_deg)),
        ),
    )
    return {"success": bool(result.success), "message": result.message, "x": float(x), "y": float(y), "yaw_deg": float(yaw_deg)}


def go_to(x: float, y: float, yaw_deg: float = 0.0):
    def configure(msg):
        msg.header.frame_id = "map"
        msg.pose.position.x = float(x)
        msg.pose.position.y = float(y)
        msg.pose.orientation.w = 1.0

    publish("/nav_goal", "geometry_msgs.msg", "PoseStamped", configure)
    return {"goal": (float(x), float(y), float(yaw_deg))}


def cancel_goal():
    raise NotImplementedError("The official navigation_controller.py does not expose a cancel-goal service.")


def is_busy():
    raise NotImplementedError("Use the Nav2 state tools on-robot to query active goal state.")


def wait_until_arrived(timeout_s: float | None = None):
    timeout_s = 120.0 if timeout_s is None else float(timeout_s)
    msg = wait_for_message("navigation_controller/reach_goal", "std_msgs.msg", "Bool", timeout=timeout_s)
    return {"arrived": bool(msg.data)}


def waypoints(points: list[tuple[float, float, float]]):
    results = []
    for x, y, yaw_deg in points:
        results.append(go_to(x, y, yaw_deg))
        wait_until_arrived()
    return {"completed": len(results), "points": points}


def status() -> dict:
    return {"goal_topic": "/nav_goal", "reach_topic": "navigation_controller/reach_goal", "set_pose_service": "navigation_controller/set_pose"}
