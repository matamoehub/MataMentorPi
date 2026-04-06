"""Obstacle avoidance helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import runtime_state
import sonar_lib

__version__ = "2.0.0"


def start(threshold_m: float = 0.45):
    state = runtime_state()
    state.avoidance_enabled = True
    state.avoidance_threshold_m = float(threshold_m)
    return step()


def stop():
    runtime_state().avoidance_enabled = False
    return {"avoidance": False}


def step():
    state = runtime_state()
    distance = sonar_lib.distance()
    action = "forward" if distance > state.avoidance_threshold_m else "turn_left"
    return {
        "avoidance": state.avoidance_enabled,
        "threshold_m": state.avoidance_threshold_m,
        "distance_m": distance,
        "action": action,
    }


def status() -> dict:
    return step()
