"""Real line-following adapter for the official MentorPi line_following node."""

from __future__ import annotations

from _mentorpi_ros import call_service, start_launch

__version__ = "3.0.0"


def _ensure_node():
    start_launch("line_following", "app", "line_following_node.launch.py")


def start(color: str = "black"):
    _ensure_node()
    call_service("line_following/enter", "std_srvs.srv", "Trigger")
    call_service(
        "line_following/set_large_model_target_color",
        "large_models_msgs.srv",
        "SetString",
        lambda req: setattr(req, "data", str(color)),
    )
    call_service("line_following/set_running", "std_srvs.srv", "SetBool", lambda req: setattr(req, "data", True))
    return {"running": True, "color": color}


def stop():
    _ensure_node()
    call_service("line_following/set_running", "std_srvs.srv", "SetBool", lambda req: setattr(req, "data", False))
    return {"running": False}


def read():
    raise NotImplementedError("The official line_following node does not expose raw line sensor reads.")


def on_line():
    raise NotImplementedError("Use line_following/image_result for visual feedback instead of fake sensor values.")


def follow_line_step():
    raise NotImplementedError("Use start(color=...) to hand control to the official line_following node.")


def set_mock_pattern(pattern: list[int]):
    raise NotImplementedError("Mock line patterns were removed.")


def status() -> dict:
    return {"services": ["line_following/enter", "line_following/set_running", "line_following/set_large_model_target_color"]}
