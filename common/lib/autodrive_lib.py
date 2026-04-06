"""Real autonomous-driving launch helpers for MentorPi."""

from __future__ import annotations

from _mentorpi_ros import start_launch

__version__ = "3.0.0"


def lane_status():
    start_launch("self_driving", "example", "self_driving/self_driving.launch.py")
    return {"launch": "self_driving/self_driving.launch.py"}


def start_lane_follow(speed: float = 0.2):
    return {"speed": speed, **lane_status()}


def stop():
    return {"note": "Stop the self-driving launch or publish zero cmd_vel from your controller."}


def detect_traffic_light():
    return {"note": "Traffic-light recognition is part of the official self_driving and yolov5 flows."}


def plan_turn(direction: str = "left"):
    return {"direction": direction, "launch": "self_driving/self_driving.launch.py"}


def parking_sequence():
    return {"launch": "self_driving/self_driving.launch.py", "feature": "parking"}


def status() -> dict:
    return {"launch": "example/example/self_driving/self_driving.launch.py"}
