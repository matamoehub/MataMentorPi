"""YOLO helpers for MataMentorPi."""

from __future__ import annotations

__version__ = "2.0.0"

_MODEL = "yolov5s"
_LABELS = ["person", "traffic light", "cone", "bottle"]


def load_model(name: str = "yolov5s"):
    global _MODEL
    _MODEL = name
    return {"model": _MODEL}


def detect(confidence_threshold: float = 0.4):
    return [
        {"label": "person", "confidence": max(0.88, confidence_threshold), "bbox": (90, 40, 220, 380)},
        {"label": "traffic light", "confidence": max(0.74, confidence_threshold), "bbox": (360, 30, 420, 180)},
    ]


def labels():
    return list(_LABELS)


def highest_confidence():
    detections = detect()
    return max(detections, key=lambda item: item["confidence"])


def status() -> dict:
    return {"model": _MODEL, "labels": labels()}
