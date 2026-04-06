"""Autonomous driving helpers for MataMentorPi."""

from __future__ import annotations

__version__ = "2.0.0"


def lane_status():
    return {"lane_center_offset_px": -12, "curvature": "gentle_left", "confidence": 0.87}


def start_lane_follow(speed: float = 0.2):
    return {"mode": "lane_follow", "speed": speed, "lane": lane_status()}


def stop():
    return {"mode": "idle"}


def detect_traffic_light():
    return {"state": "green", "confidence": 0.82}


def plan_turn(direction: str = "left"):
    return {"turn": direction, "steps": ["slow_down", f"signal_{direction}", f"turn_{direction}", "straighten"]}


def parking_sequence():
    return ["scan_space", "align", "reverse", "straighten", "stop"]


def status() -> dict:
    return {"lane": lane_status(), "traffic_light": detect_traffic_light()}
