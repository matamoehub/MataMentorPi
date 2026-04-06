"""Real YOLO helpers backed by MentorPi yolov5_ros2."""

from __future__ import annotations

from _mentorpi_ros import call_service, start_launch, wait_for_message

__version__ = "3.0.0"

_MODEL = "traffic_signs_640s_7_0"


def load_model(name: str = "traffic_signs_640s_7_0"):
    global _MODEL
    _MODEL = name
    return {"model": _MODEL}


def _ensure_node():
    start_launch("yolov5_ros2", "yolov5_ros2", "yolov5_ros2.launch.py")


def detect(confidence_threshold: float = 0.4):
    _ensure_node()
    call_service("/yolov5/start", "std_srvs.srv", "Trigger")
    msg = wait_for_message("/yolov5_ros2/object_detect", "interfaces.msg", "ObjectsInfo", timeout=5.0)
    objects = []
    for obj in msg.objects:
        objects.append({"label": obj.class_name, "confidence": float(obj.score), "bbox": tuple(obj.box)})
    return [obj for obj in objects if obj["confidence"] >= confidence_threshold]


def labels():
    return [item["label"] for item in detect(confidence_threshold=0.0)]


def highest_confidence():
    detections = detect(confidence_threshold=0.0)
    return max(detections, key=lambda item: item["confidence"])


def status() -> dict:
    return {"start_service": "/yolov5/start", "result_topic": "/yolov5_ros2/object_detect", "model": _MODEL}
