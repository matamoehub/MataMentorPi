"""Real SLAM helpers backed by MentorPi slam launch files and map tools."""

from __future__ import annotations

import os
import subprocess

from _mentorpi_ros import MentorPiIntegrationError, start_launch, stop_launch

__version__ = "3.0.0"


def start_mapping(mode: str = "2d"):
    if mode == "2d":
        return {"pid": start_launch("slam_mapping", "slam", "slam.launch.py"), "mode": mode}
    if mode == "rtabmap":
        return {"pid": start_launch("slam_mapping", "slam", "rtabmap_slam.launch.py"), "mode": mode}
    raise ValueError(f"Unsupported mapping mode: {mode}")


def stop_mapping():
    stop_launch("slam_mapping")
    return {"stopped": True}


def save_map(name: str):
    maps_dir = os.environ.get("MENTORPI_SLAM_MAP_DIR", "/home/ubuntu/ros2_ws/src/slam/maps")
    target = os.path.join(maps_dir, name)
    try:
        subprocess.run(
            ["bash", "-lc", f'ros2 run nav2_map_server map_saver_cli -f "{target}" --ros-args -p map_subscribe_transient_local:=true'],
            check=True,
            capture_output=True,
            text=True,
        )
    except Exception as exc:
        raise MentorPiIntegrationError(f"Failed to save map '{name}'.") from exc
    return {"saved": True, "map_name": name, "path_prefix": target}


def start_rtabmap():
    return start_mapping(mode="rtabmap")


def stop_rtabmap():
    return stop_mapping()


def map_status():
    return {"launch_key": "slam_mapping"}


def status() -> dict:
    return map_status()
