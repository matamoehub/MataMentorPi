"""Real camera pan/tilt helpers backed by PWM servo commands."""

from __future__ import annotations

from _mentorpi_ros import publish_servo_positions

__version__ = "3.0.0"

YAW_SERVO_ID = 1
PITCH_SERVO_ID = 2
CENTER_PULSE = 1500
PULSE_PER_DEGREE = 11


def _pulse(center: int, degrees: int, low: int = 500, high: int = 2500) -> int:
    value = int(center + degrees * PULSE_PER_DEGREE)
    return max(low, min(high, value))


def set_yaw(angle: int):
    pulse = _pulse(CENTER_PULSE, int(angle))
    publish_servo_positions([(YAW_SERVO_ID, pulse)])
    return pulse


def set_pitch(angle: int):
    pulse = _pulse(CENTER_PULSE, -int(angle))
    publish_servo_positions([(PITCH_SERVO_ID, pulse)])
    return pulse


def center_all():
    publish_servo_positions([(YAW_SERVO_ID, CENTER_PULSE), (PITCH_SERVO_ID, CENTER_PULSE)])
    return {"yaw_pulse": CENTER_PULSE, "pitch_pulse": CENTER_PULSE}


def glance_left(amplitude: int = 20, hold_s: float = 0.15):
    return {"yaw_pulse": set_yaw(-abs(amplitude)), "hold_s": hold_s}


def glance_right(amplitude: int = 20, hold_s: float = 0.15):
    return {"yaw_pulse": set_yaw(abs(amplitude)), "hold_s": hold_s}


def look_up(amplitude: int = 12, hold_s: float = 0.15):
    return {"pitch_pulse": set_pitch(abs(amplitude)), "hold_s": hold_s}


def look_down(amplitude: int = 12, hold_s: float = 0.15):
    return {"pitch_pulse": set_pitch(-abs(amplitude)), "hold_s": hold_s}


def nod(depth: int = 12, speed_s: float | None = None):
    sequence = [set_pitch(depth), set_pitch(-depth), set_pitch(0)]
    return {"sequence": sequence, "speed_s": speed_s or 0.2}


def shake(width: int = 20, speed_s: float | None = None):
    sequence = [set_yaw(-width), set_yaw(width), set_yaw(0)]
    return {"sequence": sequence, "speed_s": speed_s or 0.2}


def wiggle(cycles: int = 2, amplitude: int = 15, speed_s: float | None = None):
    sequence = []
    for _ in range(max(1, int(cycles))):
        sequence.extend([set_yaw(-amplitude), set_yaw(amplitude)])
    sequence.append(set_yaw(0))
    return {"sequence": sequence, "speed_s": speed_s or 0.2}


def tiny_wiggle(seconds: float = 2.0, amplitude: int = 8, speed_s: float = 0.12):
    return wiggle(cycles=max(1, int(seconds / max(speed_s, 0.05) / 2)), amplitude=amplitude, speed_s=speed_s)


def status() -> dict:
    return {"yaw_servo_id": YAW_SERVO_ID, "pitch_servo_id": PITCH_SERVO_ID}
