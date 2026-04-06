"""Aggregate V2-style student robot API for MataMentorPi."""

from __future__ import annotations

import builtins
import threading

import avoidance_lib
import autodrive_lib
import buzzer_lib
import camera_lib
import depth_camera_lib
import eyes_lib
import infrared_lib
import lidar_lib
import line_follower_lib
import mediapipe_lib
import mentor_ai_lib
import multi_robot_lib
import navigation_lib
import qrcode_lib
import robot_moves
import slam_lib
import sonar_lib
import tracking_lib
import tts_lib
import vision_lib
import yolo_lib

__version__ = "3.0.0"

_ROBOT_KEY = "_matamentorpi_robot_v3_singleton"
_LOCK_KEY = "_matamentorpi_robot_v3_lock"


def _lock() -> threading.Lock:
    lock = getattr(builtins, _LOCK_KEY, None)
    if lock is None:
        lock = threading.Lock()
        setattr(builtins, _LOCK_KEY, lock)
    return lock


class _ModuleNamespace:
    def __init__(self, module, *, aliases: dict[str, str] | None = None):
        self._module = module
        self._aliases = aliases or {}

    def __getattr__(self, name: str):
        target = self._aliases.get(name, name)
        return getattr(self._module, target)

    def status(self):
        fn = getattr(self._module, "status", None)
        return fn() if callable(fn) else {"module": self._module.__name__}


class RobotV3:
    def __init__(self):
        self.move = _ModuleNamespace(robot_moves)
        self.eyes = _ModuleNamespace(eyes_lib, aliases={"left": "set_left", "right": "set_right", "set_color": "set_both"})
        self.camera = _ModuleNamespace(camera_lib, aliases={"center": "center_all", "left": "glance_left", "right": "glance_right", "up": "look_up", "down": "look_down"})
        self.vision = _ModuleNamespace(vision_lib)
        self.voice = _ModuleNamespace(tts_lib, aliases={"speak": "say"})
        self.buzzer = _ModuleNamespace(buzzer_lib)
        self.sonar = _ModuleNamespace(sonar_lib)
        self.infrared = _ModuleNamespace(infrared_lib)
        self.line = _ModuleNamespace(line_follower_lib)
        self.tracking = _ModuleNamespace(tracking_lib)
        self.avoidance = _ModuleNamespace(avoidance_lib)
        self.qrcode = _ModuleNamespace(qrcode_lib)
        self.lidar = _ModuleNamespace(lidar_lib)
        self.depth = _ModuleNamespace(depth_camera_lib)
        self.slam = _ModuleNamespace(slam_lib)
        self.nav = _ModuleNamespace(navigation_lib)
        self.mediapipe = _ModuleNamespace(mediapipe_lib)
        self.yolo = _ModuleNamespace(yolo_lib)
        self.autodrive = _ModuleNamespace(autodrive_lib)
        self.multi = _ModuleNamespace(multi_robot_lib)
        self.ai = _ModuleNamespace(mentor_ai_lib)

    def status(self) -> dict:
        return {
            "move": self.move.status(),
            "lidar": self.lidar.status(),
            "depth": self.depth.status(),
            "slam": self.slam.status(),
            "nav": self.nav.status(),
            "ai": self.ai.status(),
        }

    def stop(self):
        robot_moves.stop()
        tracking_lib.stop()
        lidar_lib.stop()
        return {"stopped": True}

    def reset(self):
        raise NotImplementedError("The real MentorPi integration layer does not support resetting robot state in-memory.")


def bot() -> RobotV3:
    with _lock():
        robot = getattr(builtins, _ROBOT_KEY, None)
        if robot is None:
            robot = RobotV3()
            setattr(builtins, _ROBOT_KEY, robot)
        return robot
