"""Line following helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import runtime_state

__version__ = "2.0.0"


def set_mock_pattern(pattern: list[int]):
    if len(pattern) != 3:
        raise ValueError("Line pattern must have exactly three sensor values.")
    runtime_state().line_pattern = [1 if int(v) else 0 for v in pattern]
    return read()


def read():
    return list(runtime_state().line_pattern)


def on_line():
    return sum(read()) >= 1


def follow_line_step():
    left, center, right = read()
    if center:
        action = "forward"
    elif left:
        action = "turn_left"
    elif right:
        action = "turn_right"
    else:
        action = "search"
    return {"pattern": read(), "action": action}


def status() -> dict:
    return {"pattern": read(), "on_line": on_line()}
