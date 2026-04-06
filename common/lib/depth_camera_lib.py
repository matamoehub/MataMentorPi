"""Depth camera helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import fake_depth_matrix, runtime_state

__version__ = "2.0.0"


def rgb_frame():
    state = runtime_state()
    return {
        "type": "rgb",
        "resolution": state.depth_resolution,
        "camera_pose": {"yaw": state.camera_yaw, "pitch": state.camera_pitch},
    }


def depth_frame():
    return {"type": "depth", "resolution": runtime_state().depth_resolution, "matrix_m": fake_depth_matrix()}


def point_cloud_snapshot():
    matrix = fake_depth_matrix(width=4, height=3)
    points = []
    for row_index, row in enumerate(matrix):
        for col_index, depth in enumerate(row):
            points.append({"x": round(col_index * 0.05, 3), "y": round(row_index * 0.05, 3), "z": depth})
    return points


def depth_at(x: int, y: int):
    matrix = fake_depth_matrix(width=8, height=6)
    return matrix[y % len(matrix)][x % len(matrix[0])]


def distance_at(x: int, y: int):
    return depth_at(x, y)


def camera_info():
    state = runtime_state()
    return {
        "resolution": state.depth_resolution,
        "depth_scale_m": state.depth_scale_m,
        "streaming": state.depth_streaming,
    }


def start_web_stream():
    runtime_state().depth_streaming = True
    return camera_info()


def stop_web_stream():
    runtime_state().depth_streaming = False
    return camera_info()


def status() -> dict:
    return camera_info()
