"""MentorPi infrared placeholder with no fake data."""

from __future__ import annotations

from _mentorpi_ros import MentorPiIntegrationError

__version__ = "3.0.0"


def set_mock_pattern(left: bool = False, center: bool = True, right: bool = False):
    raise NotImplementedError("Mock infrared values were removed.")


def read():
    raise MentorPiIntegrationError("No official standalone infrared topic/service was identified in the public MentorPi repo.")


def blocked():
    raise MentorPiIntegrationError("No official standalone infrared topic/service was identified in the public MentorPi repo.")


def status() -> dict:
    return {"available": False, "reason": "No public standalone infrared interface in official repo audit"}
