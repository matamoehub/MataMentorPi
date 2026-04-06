"""Simulator state scaffold for MataMentorPi."""

from __future__ import annotations

from typing import Any


def default_state() -> dict[str, Any]:
    return {
        "version": 1,
        "robot": {"x": 0.0, "y": 0.0, "heading_deg": 0.0},
        "lidar": {"ranges": []},
        "depth": {"distance_m": None},
        "map": {"id": "default", "cells": []},
        "nav": {"goal": None, "path": []},
        "events": [],
    }

