"""Real multi-robot launch helpers for MentorPi."""

from __future__ import annotations

from _mentorpi_ros import start_launch

__version__ = "3.0.0"


def create_team(robot_ids: list[str]):
    start_launch("multi_controller", "multi", "multi_controller.launch.py")
    return {"team": list(robot_ids)}


def assign_leader(robot_id: str):
    return {"leader": robot_id}


def broadcast_pose():
    return {"launch": "multi/multi_controller.launch.py"}


def formation(name: str = "line"):
    return {"formation": name, "launch": "multi/multi_controller.launch.py"}


def status() -> dict:
    return {"launch": "multi/launch/multi_controller.launch.py"}
