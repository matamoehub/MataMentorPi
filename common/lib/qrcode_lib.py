"""QR code helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import runtime_state

__version__ = "2.0.0"


def set_mock_codes(codes: list[str]):
    runtime_state().qrcode_codes = list(codes)
    runtime_state().qrcode_index = 0
    return status()


def scan():
    state = runtime_state()
    if not state.qrcode_codes:
        return None
    code = state.qrcode_codes[state.qrcode_index % len(state.qrcode_codes)]
    state.qrcode_index += 1
    return code


def scan_all(limit: int = 3):
    return [scan() for _ in range(max(1, int(limit)))]


def status() -> dict:
    state = runtime_state()
    return {"available": list(state.qrcode_codes), "next_index": state.qrcode_index}
