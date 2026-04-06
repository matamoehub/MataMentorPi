"""Real QR detection using the MentorPi camera stream."""

from __future__ import annotations

import cv2

from _mentorpi_ros import current_image

__version__ = "3.0.0"


def scan():
    image = current_image()
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(image)
    return data or None


def scan_all(limit: int = 3):
    result = scan()
    return [result] if result else []


def set_mock_codes(codes: list[str]):
    raise NotImplementedError("Mock QR codes were removed. Use a real camera frame and QRCodeDetector.")


def status() -> dict:
    return {"camera_topic": "/ascamera/camera_publisher/rgb0/image"}
