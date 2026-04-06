"""Camera pan/tilt helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import clamp, runtime_state

__version__ = "2.0.0"


def set_yaw(angle: int):
    runtime_state().camera_yaw = int(clamp(angle, -90, 90))
    return runtime_state().camera_yaw


def set_pitch(angle: int):
    runtime_state().camera_pitch = int(clamp(angle, -45, 45))
    return runtime_state().camera_pitch


def center_all():
    state = runtime_state()
    state.camera_yaw = 0
    state.camera_pitch = 0
    return {"yaw": 0, "pitch": 0}


def glance_left(amplitude: int = 25, hold_s: float = 0.15):
    return {"yaw": set_yaw(-abs(amplitude)), "hold_s": hold_s}


def glance_right(amplitude: int = 25, hold_s: float = 0.15):
    return {"yaw": set_yaw(abs(amplitude)), "hold_s": hold_s}


def look_up(amplitude: int = 20, hold_s: float = 0.15):
    return {"pitch": set_pitch(abs(amplitude)), "hold_s": hold_s}


def look_down(amplitude: int = 20, hold_s: float = 0.15):
    return {"pitch": set_pitch(-abs(amplitude)), "hold_s": hold_s}


def nod(depth: int = 18, speed_s: float | None = None):
    return {"sequence": [set_pitch(abs(depth)), set_pitch(-abs(depth)), set_pitch(0)], "speed_s": speed_s or 0.25}


def shake(width: int = 25, speed_s: float | None = None):
    return {"sequence": [set_yaw(-abs(width)), set_yaw(abs(width)), set_yaw(0)], "speed_s": speed_s or 0.25}


def wiggle(cycles: int = 2, amplitude: int = 18, speed_s: float | None = None):
    sequence = []
    for _ in range(max(1, int(cycles))):
        sequence.extend([set_yaw(-abs(amplitude)), set_yaw(abs(amplitude))])
    sequence.append(set_yaw(0))
    return {"sequence": sequence, "speed_s": speed_s or 0.2}


def tiny_wiggle(seconds: float = 2.0, amplitude: int = 10, speed_s: float = 0.12):
    cycles = max(1, int(seconds / max(speed_s, 0.05) / 2))
    return wiggle(cycles=cycles, amplitude=amplitude, speed_s=speed_s)


def status() -> dict:
    state = runtime_state()
    return {"yaw": state.camera_yaw, "pitch": state.camera_pitch}
