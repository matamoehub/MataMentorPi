"""Text-to-speech helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import runtime_state

__version__ = "2.0.0"


def say(text: str, voice: str = "mentorpi"):
    message = f"{voice}: {text}"
    runtime_state().spoken.append(message)
    return message


def ask(question: str):
    return say(question)


def conversation():
    return list(runtime_state().spoken)


def status() -> dict:
    spoken = runtime_state().spoken
    return {"count": len(spoken), "last": spoken[-1] if spoken else None}
