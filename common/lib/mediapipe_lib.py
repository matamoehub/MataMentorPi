"""MediaPipe helpers for MataMentorPi."""

from __future__ import annotations

__version__ = "2.0.0"


def detect_hands():
    return [{"label": "right", "confidence": 0.96, "center": (0.58, 0.42)}]


def detect_pose():
    return {"pose_detected": True, "confidence": 0.93, "landmarks": 17}


def detect_face():
    return {"faces": 1, "confidence": 0.91}


def follow_hand():
    hand = detect_hands()[0]
    return {"target": hand["label"], "command": "turn_right" if hand["center"][0] > 0.5 else "turn_left"}


def finger_trajectory():
    return {"points": [(0.2, 0.4), (0.35, 0.32), (0.52, 0.28), (0.7, 0.4)], "gesture": "arc"}


def body_control():
    return {"pose": "arms_up", "robot_action": "celebrate"}


def fall_detection():
    return {"fall_detected": False, "confidence": 0.04}


def status() -> dict:
    return {"hands": len(detect_hands()), "pose_detected": detect_pose()["pose_detected"]}
