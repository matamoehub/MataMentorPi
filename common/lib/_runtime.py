"""Shared in-memory runtime for MataMentorPi teaching libraries."""

from __future__ import annotations

import builtins
import math
import threading
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

_STATE_KEY = "_matamentorpi_runtime_state"
_LOCK_KEY = "_matamentorpi_runtime_lock"


@dataclass
class RuntimeState:
    move_base_speed: float = 0.3
    move_rate_hz: float = 20.0
    pose_x: float = 0.0
    pose_y: float = 0.0
    yaw_deg: float = 0.0
    last_motion: str = "stopped"
    eyes_left: Tuple[int, int, int] = (0, 255, 120)
    eyes_right: Tuple[int, int, int] = (0, 255, 120)
    blinking: bool = False
    camera_yaw: int = 0
    camera_pitch: int = 0
    spoken: List[str] = field(default_factory=list)
    buzzer_events: List[str] = field(default_factory=list)
    sonar_distance_m: float = 1.2
    infrared: Dict[str, bool] = field(
        default_factory=lambda: {"left": False, "center": True, "right": False}
    )
    line_pattern: List[int] = field(default_factory=lambda: [0, 1, 0])
    tracking_target: Optional[str] = None
    tracking_active: bool = False
    qrcode_codes: List[str] = field(default_factory=lambda: ["MENTOR-PI"])
    qrcode_index: int = 0
    avoidance_enabled: bool = False
    avoidance_threshold_m: float = 0.45
    lidar_mode: str = "idle"
    lidar_running: bool = False
    lidar_threshold_m: float = 0.6
    lidar_scan_angle_deg: int = 90
    lidar_speed: float = 0.2
    depth_streaming: bool = False
    depth_resolution: Tuple[int, int] = (640, 480)
    depth_scale_m: float = 0.001
    slam_mode: str = "idle"
    slam_map_name: Optional[str] = None
    nav_active: bool = False
    nav_map_name: Optional[str] = None
    nav_goal: Optional[Tuple[float, float, float]] = None
    nav_waypoints: List[Tuple[float, float, float]] = field(default_factory=list)
    multi_team: List[str] = field(default_factory=lambda: ["mentorpi-1"])
    multi_leader: str = "mentorpi-1"
    ai_awake: bool = False
    history: List[str] = field(default_factory=list)


def runtime_lock() -> threading.Lock:
    lock = getattr(builtins, _LOCK_KEY, None)
    if lock is None:
        lock = threading.Lock()
        setattr(builtins, _LOCK_KEY, lock)
    return lock


def runtime_state() -> RuntimeState:
    with runtime_lock():
        state = getattr(builtins, _STATE_KEY, None)
        if state is None:
            state = RuntimeState()
            setattr(builtins, _STATE_KEY, state)
        return state


def log_event(message: str) -> str:
    state = runtime_state()
    stamp = time.strftime("%H:%M:%S")
    entry = f"[{stamp}] {message}"
    state.history.append(entry)
    return entry


def status_snapshot() -> Dict[str, Any]:
    state = runtime_state()
    return {
        "pose": {"x": round(state.pose_x, 3), "y": round(state.pose_y, 3), "yaw_deg": round(state.yaw_deg, 1)},
        "last_motion": state.last_motion,
        "lidar_mode": state.lidar_mode,
        "slam_mode": state.slam_mode,
        "nav_active": state.nav_active,
        "tracking_active": state.tracking_active,
        "ai_awake": state.ai_awake,
    }


def reset_runtime() -> Dict[str, Any]:
    with runtime_lock():
        setattr(builtins, _STATE_KEY, RuntimeState())
    return status_snapshot()


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, float(value)))


def normalize_yaw(yaw_deg: float) -> float:
    yaw = float(yaw_deg) % 360.0
    return yaw if yaw < 180.0 else yaw - 360.0


def advance_pose(forward_m: float = 0.0, lateral_m: float = 0.0, turn_deg: float = 0.0) -> Dict[str, float]:
    state = runtime_state()
    yaw_rad = math.radians(state.yaw_deg)
    dx = forward_m * math.cos(yaw_rad) - lateral_m * math.sin(yaw_rad)
    dy = forward_m * math.sin(yaw_rad) + lateral_m * math.cos(yaw_rad)
    state.pose_x += dx
    state.pose_y += dy
    state.yaw_deg = normalize_yaw(state.yaw_deg + turn_deg)
    return {"x": round(state.pose_x, 3), "y": round(state.pose_y, 3), "yaw_deg": round(state.yaw_deg, 1)}


def fake_scan(samples: int = 9) -> List[Dict[str, float]]:
    state = runtime_state()
    half_angle = state.lidar_scan_angle_deg / 2.0
    readings: List[Dict[str, float]] = []
    for index in range(max(3, int(samples))):
        fraction = index / max(1, samples - 1)
        angle = -half_angle + fraction * state.lidar_scan_angle_deg
        distance = max(0.15, state.sonar_distance_m + abs(angle) / 180.0 * 0.4)
        readings.append({"angle_deg": round(angle, 1), "distance_m": round(distance, 3)})
    return readings


def fake_depth_matrix(width: int = 6, height: int = 4) -> List[List[float]]:
    state = runtime_state()
    base = max(0.2, state.sonar_distance_m)
    return [
        [round(base + row * 0.08 + col * 0.03, 3) for col in range(width)]
        for row in range(height)
    ]
