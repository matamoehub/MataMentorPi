"""Real depth camera helpers backed by MentorPi ascamera topics."""

from __future__ import annotations

from _mentorpi_ros import current_depth_image, current_image, start_launch, wait_for_message

__version__ = "3.0.0"


def ensure_depth_camera():
    return start_launch("depth_camera", "peripherals", "depth_camera.launch.py")


def rgb_frame():
    ensure_depth_camera()
    image = current_image()
    return image


def depth_frame():
    ensure_depth_camera()
    return current_depth_image()


def point_cloud_snapshot():
    ensure_depth_camera()
    depth = current_depth_image()
    samples = []
    step_y = max(1, depth.shape[0] // 6)
    step_x = max(1, depth.shape[1] // 6)
    for y in range(0, depth.shape[0], step_y):
        for x in range(0, depth.shape[1], step_x):
            z = float(depth[y, x]) / 1000.0
            samples.append({"x": x, "y": y, "z_m": z})
    return samples


def depth_at(x: int, y: int):
    ensure_depth_camera()
    depth = current_depth_image()
    return int(depth[int(y), int(x)])


def distance_at(x: int, y: int):
    return depth_at(x, y) / 1000.0


def camera_info():
    ensure_depth_camera()
    msg = wait_for_message("/ascamera/camera_publisher/rgb0/camera_info", "sensor_msgs.msg", "CameraInfo", timeout=3.0)
    return {"width": int(msg.width), "height": int(msg.height), "distortion_model": msg.distortion_model}


def start_web_stream():
    return ensure_depth_camera()


def stop_web_stream():
    raise NotImplementedError("The official depth_camera launch does not expose a dedicated stop-stream service.")


def status() -> dict:
    return {"rgb_topic": "/ascamera/camera_publisher/rgb0/image", "depth_topic": "/ascamera/camera_publisher/depth0/image_raw"}
