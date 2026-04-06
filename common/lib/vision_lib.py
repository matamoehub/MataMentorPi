"""Real vision helpers using the MentorPi RGB camera stream."""

from __future__ import annotations

import cv2
import numpy as np

from _mentorpi_ros import current_image

__version__ = "3.0.0"


def capture(show: bool = True, save_path: str | None = None, title: str = "MentorPi Capture"):
    image = current_image()
    if save_path:
        cv2.imwrite(save_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    return {"title": title, "shape": tuple(image.shape), "save_path": save_path, "show": show}


def detect_color(color: str = "red", min_area: int = 500):
    image = current_image()
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    ranges = {
        "red": [((0, 120, 70), (10, 255, 255)), ((170, 120, 70), (180, 255, 255))],
        "green": [((35, 70, 50), (85, 255, 255))],
        "blue": [((90, 70, 50), (130, 255, 255))],
        "yellow": [((20, 100, 100), (35, 255, 255))],
        "black": [((0, 0, 0), (180, 255, 60))],
    }
    masks = [cv2.inRange(hsv, np.array(low), np.array(high)) for low, high in ranges[color.lower()]]
    mask = masks[0]
    for extra in masks[1:]:
        mask = cv2.bitwise_or(mask, extra)
    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    if not contours:
        return {"color": color, "found": False}
    contour = max(contours, key=cv2.contourArea)
    area = int(cv2.contourArea(contour))
    if area < int(min_area):
        return {"color": color, "found": False, "area": area}
    x, y, w, h = cv2.boundingRect(contour)
    return {"color": color, "found": True, "area": area, "center": (x + w // 2, y + h // 2), "bbox": (x, y, x + w, y + h)}


def show_color(color: str, show: bool = True, save_path: str | None = None, min_area: int | None = None):
    result = detect_color(color=color, min_area=min_area or 500)
    result.update({"show": show, "save_path": save_path})
    return result


def largest_blob(color: str = "green"):
    return detect_color(color=color)


def status() -> dict:
    return {"camera_topic": "/ascamera/camera_publisher/rgb0/image"}
