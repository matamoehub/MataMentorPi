"""Real object tracking adapter for the official MentorPi object_tracking node."""

from __future__ import annotations

from _mentorpi_ros import call_service, start_launch

__version__ = "3.0.0"


def _ensure_node():
    start_launch("object_tracking", "app", "object_tracking_node.launch.py")


def start(target: str = "red"):
    _ensure_node()
    call_service("object_tracking/enter", "std_srvs.srv", "Trigger")
    call_service(
        "object_tracking/set_large_model_target_color",
        "large_models_msgs.srv",
        "SetString",
        lambda req: setattr(req, "data", str(target)),
    )
    call_service("object_tracking/set_running", "std_srvs.srv", "SetBool", lambda req: setattr(req, "data", True))
    return {"tracking": True, "target": target}


def stop():
    _ensure_node()
    call_service("object_tracking/set_running", "std_srvs.srv", "SetBool", lambda req: setattr(req, "data", False))
    return {"tracking": False}


def target():
    raise NotImplementedError("The official object_tracking node does not expose a target query service.")


def step():
    raise NotImplementedError("Use the official object_tracking/image_result and motion topics for live tracking feedback.")


def status() -> dict:
    return {"services": ["object_tracking/enter", "object_tracking/set_running", "object_tracking/set_large_model_target_color"]}
