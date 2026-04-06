"""Buzzer and sound helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import runtime_state

__version__ = "2.0.0"


def beep(duration_s: float = 0.2, pitch: str = "A4"):
    event = f"beep:{pitch}:{round(duration_s, 2)}"
    runtime_state().buzzer_events.append(event)
    return event


def horn(times: int = 1):
    events = [beep(duration_s=0.3, pitch="C5") for _ in range(max(1, int(times)))]
    return {"horn": events}


def celebrate():
    tune = [beep(0.15, "C5"), beep(0.15, "E5"), beep(0.25, "G5")]
    return {"celebrate": tune}


def status() -> dict:
    return {"recent": runtime_state().buzzer_events[-10:]}
