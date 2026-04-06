"""RGB eye helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import clamp, runtime_state

__version__ = "2.0.0"


def _rgb(r: int, g: int | None = None, b: int | None = None):
    if isinstance(r, (tuple, list)):
        r, g, b = r
    if g is None or b is None:
        raise TypeError("Expected either an RGB tuple or three integer channels.")
    return (
        int(clamp(r, 0, 255)),
        int(clamp(g, 0, 255)),
        int(clamp(b, 0, 255)),
    )


def set_left(r: int, g: int | None = None, b: int | None = None):
    runtime_state().eyes_left = _rgb(r, g, b)
    return runtime_state().eyes_left


def set_right(r: int, g: int | None = None, b: int | None = None):
    runtime_state().eyes_right = _rgb(r, g, b)
    return runtime_state().eyes_right


def set_both(r: int, g: int | None = None, b: int | None = None):
    rgb = _rgb(r, g, b)
    runtime_state().eyes_left = rgb
    runtime_state().eyes_right = rgb
    return rgb


def color(r: int, g: int | None = None, b: int | None = None):
    return set_both(r, g, b)


def off():
    return set_both(0, 0, 0)


def on(r: int = 0, g: int = 255, b: int = 120):
    return set_both(r, g, b)


def blink(every_s: float = 3.0, blank_s: float = 0.5):
    runtime_state().blinking = True
    return {"blinking": True, "every_s": every_s, "blank_s": blank_s}


def blink_once(blank_s: float = 0.5):
    return {"blink_once": True, "blank_s": blank_s}


def stop_blink():
    runtime_state().blinking = False
    return {"blinking": False}


def wink(side: str = "left", blank_s: float = 0.5):
    return {"side": side, "blank_s": blank_s}


def status() -> dict:
    state = runtime_state()
    return {
        "left": state.eyes_left,
        "right": state.eyes_right,
        "blinking": state.blinking,
    }
