"""V2-style movement helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import advance_pose, clamp, log_event, runtime_state, status_snapshot

__version__ = "2.0.0"


def set_base_speed(speed: float):
    runtime_state().move_base_speed = clamp(speed, 0.05, 2.0)
    return runtime_state().move_base_speed


def set_rate(hz: float):
    runtime_state().move_rate_hz = clamp(hz, 1.0, 60.0)
    return runtime_state().move_rate_hz


def _distance(seconds: float, speed: float | None) -> float:
    state = runtime_state()
    metres_per_second = state.move_base_speed if speed is None else clamp(speed, 0.05, 2.0)
    return round(max(0.0, float(seconds)) * metres_per_second, 3)


def stop():
    runtime_state().last_motion = "stopped"
    return log_event("Movement stopped")


def emergency_stop():
    return stop()


def forward(seconds: float = 0.5, speed: float | None = None):
    travelled = _distance(seconds, speed)
    runtime_state().last_motion = "forward"
    pose = advance_pose(forward_m=travelled)
    return {"move": "forward", "distance_m": travelled, "pose": pose}


def backward(seconds: float = 0.5, speed: float | None = None):
    travelled = _distance(seconds, speed)
    runtime_state().last_motion = "backward"
    pose = advance_pose(forward_m=-travelled)
    return {"move": "backward", "distance_m": travelled, "pose": pose}


def left(seconds: float = 0.5, speed: float | None = None):
    travelled = _distance(seconds, speed)
    runtime_state().last_motion = "left"
    pose = advance_pose(lateral_m=-travelled)
    return {"move": "left", "distance_m": travelled, "pose": pose}


def right(seconds: float = 0.5, speed: float | None = None):
    travelled = _distance(seconds, speed)
    runtime_state().last_motion = "right"
    pose = advance_pose(lateral_m=travelled)
    return {"move": "right", "distance_m": travelled, "pose": pose}


def turn_left(seconds: float = 0.5, speed: float | None = None):
    degrees = round(_distance(seconds, speed) * 90.0, 1)
    runtime_state().last_motion = "turn_left"
    pose = advance_pose(turn_deg=degrees)
    return {"move": "turn_left", "turn_deg": degrees, "pose": pose}


def turn_right(seconds: float = 0.5, speed: float | None = None):
    degrees = round(_distance(seconds, speed) * 90.0, 1)
    runtime_state().last_motion = "turn_right"
    pose = advance_pose(turn_deg=-degrees)
    return {"move": "turn_right", "turn_deg": degrees, "pose": pose}


def diagonal_left(seconds: float = 0.8, speed: float | None = None):
    travelled = _distance(seconds, speed)
    runtime_state().last_motion = "diagonal_left"
    pose = advance_pose(forward_m=travelled, lateral_m=-travelled)
    return {"move": "diagonal_left", "distance_m": travelled, "pose": pose}


def diagonal_right(seconds: float = 0.8, speed: float | None = None):
    travelled = _distance(seconds, speed)
    runtime_state().last_motion = "diagonal_right"
    pose = advance_pose(forward_m=travelled, lateral_m=travelled)
    return {"move": "diagonal_right", "distance_m": travelled, "pose": pose}


def drift_left(seconds: float = 1.0, speed: float | None = None, turn_blend: float = 0.55):
    travelled = _distance(seconds, speed)
    runtime_state().last_motion = "drift_left"
    pose = advance_pose(lateral_m=-travelled, turn_deg=45.0 * clamp(turn_blend, 0.0, 1.0))
    return {"move": "drift_left", "distance_m": travelled, "turn_blend": clamp(turn_blend, 0.0, 1.0), "pose": pose}


def drift_right(seconds: float = 1.0, speed: float | None = None, turn_blend: float = 0.55):
    travelled = _distance(seconds, speed)
    runtime_state().last_motion = "drift_right"
    pose = advance_pose(lateral_m=travelled, turn_deg=-45.0 * clamp(turn_blend, 0.0, 1.0))
    return {"move": "drift_right", "distance_m": travelled, "turn_blend": clamp(turn_blend, 0.0, 1.0), "pose": pose}


def drive_for(vx: float, vy: float, seconds: float, speed: float | None = None):
    distance = _distance(seconds, speed)
    runtime_state().last_motion = "drive_for"
    pose = advance_pose(
        forward_m=distance * clamp(vx, -1.0, 1.0),
        lateral_m=distance * clamp(vy, -1.0, 1.0),
    )
    return {"move": "drive_for", "vx": clamp(vx, -1.0, 1.0), "vy": clamp(vy, -1.0, 1.0), "pose": pose}


def pose():
    snapshot = status_snapshot()["pose"]
    return snapshot


def demo_square(side_seconds: float = 1.0, speed: float | None = None):
    steps = []
    for _ in range(4):
        steps.append(forward(seconds=side_seconds, speed=speed))
        steps.append(turn_left(seconds=0.8, speed=speed))
    return steps


def status() -> dict:
    state = runtime_state()
    return {
        **status_snapshot(),
        "base_speed_mps": state.move_base_speed,
        "rate_hz": state.move_rate_hz,
    }
