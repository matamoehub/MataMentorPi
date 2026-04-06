"""Vision helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import runtime_state

__version__ = "2.0.0"


def capture(show: bool = True, save_path: str | None = None, title: str = "MentorPi Capture"):
    state = runtime_state()
    return {
        "title": title,
        "show": show,
        "save_path": save_path,
        "camera": {"yaw": state.camera_yaw, "pitch": state.camera_pitch},
    }


def detect_color(color: str = "red", min_area: int = 500):
    return {"color": color.lower(), "found": True, "area": max(800, int(min_area)), "center": (320, 240)}


def show_color(color: str, show: bool = True, save_path: str | None = None, min_area: int | None = None):
    result = detect_color(color=color, min_area=min_area or 500)
    result.update({"show": show, "save_path": save_path})
    return result


def largest_blob(color: str = "green"):
    return detect_color(color=color)


def status() -> dict:
    return {"camera_ready": True, "tracking_target": runtime_state().tracking_target}
