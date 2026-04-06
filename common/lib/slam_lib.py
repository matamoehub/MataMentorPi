"""SLAM helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import runtime_state

__version__ = "2.0.0"


def start_mapping(mode: str = "2d"):
    state = runtime_state()
    state.slam_mode = f"mapping:{mode}"
    return map_status()


def stop_mapping():
    runtime_state().slam_mode = "idle"
    return map_status()


def save_map(name: str):
    runtime_state().slam_map_name = name
    return {"saved": True, "map_name": name, "slam_mode": runtime_state().slam_mode}


def start_rtabmap():
    runtime_state().slam_mode = "mapping:rtabmap"
    return map_status()


def stop_rtabmap():
    return stop_mapping()


def map_status():
    state = runtime_state()
    return {"slam_mode": state.slam_mode, "map_name": state.slam_map_name}


def status() -> dict:
    return map_status()
