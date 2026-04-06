"""Infrared helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import runtime_state

__version__ = "2.0.0"


def set_mock_pattern(left: bool = False, center: bool = True, right: bool = False):
    runtime_state().infrared = {"left": bool(left), "center": bool(center), "right": bool(right)}
    return status()


def read():
    return dict(runtime_state().infrared)


def blocked():
    values = read()
    return any(values.values())


def status() -> dict:
    values = read()
    values["blocked"] = blocked()
    return values
