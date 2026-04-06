"""Real TTS helpers backed by MentorPi tts_node."""

from __future__ import annotations

from _mentorpi_ros import publish_text, start_launch

__version__ = "3.0.0"


def ensure_tts():
    return start_launch("mentorpi_tts", "large_models", "tts_node.launch.py")


def say(text: str, voice: str = "mentorpi"):
    ensure_tts()
    publish_text("tts_node/tts_text", text)
    return {"voice": voice, "text": text}


def ask(question: str):
    return say(question)


def conversation():
    raise NotImplementedError("MentorPi tts_node publishes speech but does not expose a conversation history service.")


def status() -> dict:
    return {"topic": "tts_node/tts_text"}
