"""Simple helpers for scaffolded libraries."""

from __future__ import annotations


def scaffold_message(module_name: str) -> str:
    return (
        f"{module_name} is scaffolded but not implemented yet. "
        "Use the implementation plan in docs/matamentorpi-implementation-plan.md."
    )

