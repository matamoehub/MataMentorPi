"""Real buzzer helpers backed by ros_robot_controller."""

from __future__ import annotations

from _mentorpi_ros import publish_buzzer

__version__ = "3.0.0"


def beep(duration_s: float = 0.2, pitch: int = 1900):
    publish_buzzer(freq=int(pitch), on_time=float(duration_s), off_time=0.05, repeat=1)
    return {"freq": int(pitch), "duration_s": float(duration_s)}


def horn(times: int = 1):
    return [beep(duration_s=0.15, pitch=2200) for _ in range(max(1, int(times)))]


def celebrate():
    return [beep(0.1, 1800), beep(0.1, 2200), beep(0.2, 2600)]


def status() -> dict:
    return {"topic": "ros_robot_controller/set_buzzer"}
