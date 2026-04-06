"""Real lidar helpers backed by the official MentorPi lidar_controller node."""

from __future__ import annotations

import math

from _mentorpi_ros import call_service, current_laserscan, start_launch

__version__ = "3.0.0"


def _ensure_node():
    start_launch("lidar_controller", "app", "lidar_node.launch.py")


def enter():
    _ensure_node()
    result = call_service("lidar_controller/enter", "std_srvs.srv", "Trigger")
    return {"success": bool(result.success), "message": result.message}


def exit():
    _ensure_node()
    result = call_service("lidar_controller/exit", "std_srvs.srv", "Trigger")
    return {"success": bool(result.success), "message": result.message}


def set_mode(mode: str):
    modes = {"idle": 0, "obstacle_avoidance": 1, "follow": 2, "guard": 3}
    if mode not in modes:
        raise ValueError(f"Unsupported lidar mode: {mode}")
    _ensure_node()
    result = call_service("lidar_controller/set_running", "interfaces.srv", "SetInt64", lambda req: setattr(req, "data", modes[mode]))
    return {"success": bool(result.success), "message": result.message, "mode": mode}


def set_params(threshold_m: float | None = None, scan_angle_deg: int | None = None, speed: float | None = None):
    threshold_m = 0.6 if threshold_m is None else float(threshold_m)
    scan_angle_deg = 90 if scan_angle_deg is None else int(scan_angle_deg)
    speed = 0.2 if speed is None else float(speed)
    _ensure_node()
    result = call_service(
        "lidar_controller/set_param",
        "interfaces.srv",
        "SetFloat64List",
        lambda req: setattr(req, "data", [threshold_m, float(scan_angle_deg), speed]),
    )
    return {"success": bool(result.success), "message": result.message, "threshold_m": threshold_m, "scan_angle_deg": scan_angle_deg, "speed": speed}


def start_obstacle_avoidance(threshold_m: float = 0.6, scan_angle_deg: int = 90, speed: float = 0.2):
    enter()
    set_params(threshold_m=threshold_m, scan_angle_deg=scan_angle_deg, speed=speed)
    return set_mode("obstacle_avoidance")


def start_follow(target_distance_m: float = 0.3, scan_angle_deg: int = 90, speed: float = 0.2):
    enter()
    set_params(threshold_m=target_distance_m, scan_angle_deg=scan_angle_deg, speed=speed)
    return set_mode("follow")


def start_guard(threshold_m: float = 0.6, scan_angle_deg: int = 90, speed: float = 0.2):
    enter()
    set_params(threshold_m=threshold_m, scan_angle_deg=scan_angle_deg, speed=speed)
    return set_mode("guard")


def stop():
    return set_mode("idle")


def scan_snapshot(samples: int = 9):
    scan = current_laserscan()
    total = len(scan.ranges)
    if total == 0:
        return []
    step = max(1, total // max(1, int(samples)))
    readings = []
    for index in range(0, total, step):
        angle = scan.angle_min + index * scan.angle_increment
        readings.append({"angle_deg": round(math.degrees(angle), 1), "distance_m": float(scan.ranges[index])})
        if len(readings) >= samples:
            break
    return readings


def status() -> dict:
    return {"services": ["lidar_controller/enter", "lidar_controller/exit", "lidar_controller/set_running", "lidar_controller/set_param"], "scan_topic": "/scan_raw"}
