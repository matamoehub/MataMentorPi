"""Real RGB eye helpers backed by ros_robot_controller."""

from __future__ import annotations

from _mentorpi_ros import publish_rgb

__version__ = "3.0.0"


def _rgb(r: int, g: int | None = None, b: int | None = None):
    if isinstance(r, (tuple, list)):
        r, g, b = r
    if g is None or b is None:
        raise TypeError("Expected an RGB tuple or three channels.")
    return int(r), int(g), int(b)


def set_left(r: int, g: int | None = None, b: int | None = None):
    rgb = _rgb(r, g, b)
    publish_rgb(rgb, (0, 0, 0))
    return rgb


def set_right(r: int, g: int | None = None, b: int | None = None):
    rgb = _rgb(r, g, b)
    publish_rgb((0, 0, 0), rgb)
    return rgb


def set_both(r: int, g: int | None = None, b: int | None = None):
    rgb = _rgb(r, g, b)
    publish_rgb(rgb, rgb)
    return rgb


def color(r: int, g: int | None = None, b: int | None = None):
    return set_both(r, g, b)


def off():
    return set_both(0, 0, 0)


def on(r: int = 0, g: int = 255, b: int = 120):
    return set_both(r, g, b)


def blink(every_s: float = 3.0, blank_s: float = 0.5):
    return {"every_s": every_s, "blank_s": blank_s, "note": "Use repeated set_both/off calls from your lesson loop."}


def blink_once(blank_s: float = 0.5):
    off()
    return {"blank_s": blank_s}


def stop_blink():
    return {"stopped": True}


def wink(side: str = "left", blank_s: float = 0.5):
    return {"side": side, "blank_s": blank_s}


def status() -> dict:
    return {"topic": "ros_robot_controller/set_rgb"}
