"""MentorPi sonar placeholder with no fake data."""

from __future__ import annotations

from _mentorpi_ros import MentorPiIntegrationError

__version__ = "3.0.0"


def set_mock_distance(distance_m: float):
    raise NotImplementedError("Mock sonar values were removed.")


def distance():
    raise MentorPiIntegrationError("No official standalone sonar topic/service was identified in the public MentorPi repo.")


def distance_cm():
    raise MentorPiIntegrationError("No official standalone sonar topic/service was identified in the public MentorPi repo.")


def is_clear(threshold_m: float = 0.4):
    raise MentorPiIntegrationError("No official standalone sonar topic/service was identified in the public MentorPi repo.")


def status() -> dict:
    return {"available": False, "reason": "No public standalone sonar interface in official repo audit"}
