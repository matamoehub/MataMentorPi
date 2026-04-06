"""Sonar helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import clamp, runtime_state

__version__ = "2.0.0"


def set_mock_distance(distance_m: float):
    runtime_state().sonar_distance_m = clamp(distance_m, 0.05, 8.0)
    return runtime_state().sonar_distance_m


def distance():
    return round(runtime_state().sonar_distance_m, 3)


def distance_cm():
    return round(distance() * 100.0, 1)


def is_clear(threshold_m: float = 0.4):
    return distance() > float(threshold_m)


def status() -> dict:
    return {"distance_m": distance(), "distance_cm": distance_cm()}
