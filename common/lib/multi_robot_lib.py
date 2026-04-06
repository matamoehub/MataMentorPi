"""Multi-robot helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import runtime_state

__version__ = "2.0.0"


def create_team(robot_ids: list[str]):
    runtime_state().multi_team = list(robot_ids)
    if robot_ids:
        runtime_state().multi_leader = robot_ids[0]
    return status()


def assign_leader(robot_id: str):
    runtime_state().multi_leader = robot_id
    return status()


def broadcast_pose():
    state = runtime_state()
    return {"leader": state.multi_leader, "pose": {"x": state.pose_x, "y": state.pose_y, "yaw_deg": state.yaw_deg}}


def formation(name: str = "line"):
    team = runtime_state().multi_team
    slots = [{"robot": robot_id, "slot": index, "formation": name} for index, robot_id in enumerate(team)]
    return {"formation": name, "members": slots}


def status() -> dict:
    state = runtime_state()
    return {"team": list(state.multi_team), "leader": state.multi_leader}
