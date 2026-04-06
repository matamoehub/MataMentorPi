"""Real movement helpers backed by MentorPi ROS2 topics."""

from __future__ import annotations

from _mentorpi_ros import current_odometry, publish_twist, yaw_from_quaternion

__version__ = "3.0.0"

_BASE_SPEED = 0.2
_TURN_SPEED = 1.0


def set_base_speed(speed: float):
    global _BASE_SPEED
    _BASE_SPEED = float(speed)
    return _BASE_SPEED


def set_rate(hz: float):
    return float(hz)


def stop():
    return publish_twist()


def emergency_stop():
    return stop()


def forward(seconds: float = 0.5, speed: float | None = None):
    return publish_twist(vx=float(_BASE_SPEED if speed is None else speed), seconds=seconds)


def backward(seconds: float = 0.5, speed: float | None = None):
    return publish_twist(vx=-float(_BASE_SPEED if speed is None else speed), seconds=seconds)


def left(seconds: float = 0.5, speed: float | None = None):
    return publish_twist(vy=-float(_BASE_SPEED if speed is None else speed), seconds=seconds)


def right(seconds: float = 0.5, speed: float | None = None):
    return publish_twist(vy=float(_BASE_SPEED if speed is None else speed), seconds=seconds)


def turn_left(seconds: float = 0.5, speed: float | None = None):
    return publish_twist(wz=float(_TURN_SPEED if speed is None else speed), seconds=seconds)


def turn_right(seconds: float = 0.5, speed: float | None = None):
    return publish_twist(wz=-float(_TURN_SPEED if speed is None else speed), seconds=seconds)


def diagonal_left(seconds: float = 0.8, speed: float | None = None):
    speed = float(_BASE_SPEED if speed is None else speed)
    return publish_twist(vx=speed, vy=-speed, seconds=seconds)


def diagonal_right(seconds: float = 0.8, speed: float | None = None):
    speed = float(_BASE_SPEED if speed is None else speed)
    return publish_twist(vx=speed, vy=speed, seconds=seconds)


def drift_left(seconds: float = 1.0, speed: float | None = None, turn_blend: float = 0.55):
    speed = float(_BASE_SPEED if speed is None else speed)
    return publish_twist(vy=-speed, wz=float(turn_blend) * _TURN_SPEED, seconds=seconds)


def drift_right(seconds: float = 1.0, speed: float | None = None, turn_blend: float = 0.55):
    speed = float(_BASE_SPEED if speed is None else speed)
    return publish_twist(vy=speed, wz=-float(turn_blend) * _TURN_SPEED, seconds=seconds)


def drive_for(vx: float, vy: float, seconds: float, speed: float | None = None):
    scale = float(_BASE_SPEED if speed is None else speed)
    return publish_twist(vx=float(vx) * scale, vy=float(vy) * scale, seconds=seconds)


def pose():
    odom = current_odometry()
    return {
        "x": round(float(odom.pose.pose.position.x), 3),
        "y": round(float(odom.pose.pose.position.y), 3),
        "yaw_deg": round(float(yaw_from_quaternion(odom.pose.pose.orientation)), 1),
    }


def status() -> dict:
    return {"pose": pose(), "base_speed": _BASE_SPEED, "turn_speed": _TURN_SPEED}
