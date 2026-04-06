"""Real avoidance adapter that delegates to the official lidar controller."""

from __future__ import annotations

import lidar_lib

__version__ = "3.0.0"


def start(threshold_m: float = 0.45):
    return lidar_lib.start_obstacle_avoidance(threshold_m=threshold_m)


def stop():
    return lidar_lib.stop()


def step():
    raise NotImplementedError("Obstacle avoidance runs inside the official lidar_controller node.")


def status() -> dict:
    return lidar_lib.status()
