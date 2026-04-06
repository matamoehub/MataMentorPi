"""Object tracking helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import runtime_state

__version__ = "2.0.0"


def start(target: str = "red ball"):
    state = runtime_state()
    state.tracking_active = True
    state.tracking_target = target
    return {"tracking": True, "target": target}


def stop():
    runtime_state().tracking_active = False
    return {"tracking": False, "target": runtime_state().tracking_target}


def target():
    return runtime_state().tracking_target


def step():
    state = runtime_state()
    return {"tracking": state.tracking_active, "target": state.tracking_target, "offset_px": (18, -9)}


def status() -> dict:
    state = runtime_state()
    return {"tracking": state.tracking_active, "target": state.tracking_target}
