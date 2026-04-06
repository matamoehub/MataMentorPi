"""Lidar helpers inspired by the official MentorPi controller apps."""

from __future__ import annotations

from _runtime import fake_scan, runtime_state

__version__ = "2.0.0"


def enter():
    runtime_state().lidar_running = True
    return {"entered": True, "mode": runtime_state().lidar_mode}


def exit():
    state = runtime_state()
    state.lidar_running = False
    state.lidar_mode = "idle"
    return {"entered": False, "mode": state.lidar_mode}


def set_mode(mode: str):
    state = runtime_state()
    state.lidar_mode = mode
    state.lidar_running = mode != "idle"
    return status()


def set_params(threshold_m: float | None = None, scan_angle_deg: int | None = None, speed: float | None = None):
    state = runtime_state()
    if threshold_m is not None:
        state.lidar_threshold_m = float(threshold_m)
    if scan_angle_deg is not None:
        state.lidar_scan_angle_deg = int(scan_angle_deg)
    if speed is not None:
        state.lidar_speed = float(speed)
    return status()


def start_obstacle_avoidance(threshold_m: float = 0.6, scan_angle_deg: int = 90, speed: float = 0.2):
    set_params(threshold_m=threshold_m, scan_angle_deg=scan_angle_deg, speed=speed)
    return set_mode("obstacle_avoidance")


def start_follow(target_distance_m: float = 0.3, scan_angle_deg: int = 90, speed: float = 0.2):
    set_params(threshold_m=target_distance_m, scan_angle_deg=scan_angle_deg, speed=speed)
    return set_mode("follow")


def start_guard(threshold_m: float = 0.6, scan_angle_deg: int = 90, speed: float = 0.2):
    set_params(threshold_m=threshold_m, scan_angle_deg=scan_angle_deg, speed=speed)
    return set_mode("guard")


def stop():
    return set_mode("idle")


def scan_snapshot(samples: int = 9):
    return fake_scan(samples=samples)


def status() -> dict:
    state = runtime_state()
    return {
        "running": state.lidar_running,
        "mode": state.lidar_mode,
        "threshold_m": state.lidar_threshold_m,
        "scan_angle_deg": state.lidar_scan_angle_deg,
        "speed": state.lidar_speed,
    }
