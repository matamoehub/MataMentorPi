"""Large-model style helpers for MataMentorPi."""

from __future__ import annotations

from _runtime import runtime_state

__version__ = "2.0.0"


def wake():
    runtime_state().ai_awake = True
    return {"awake": True}


def sleep():
    runtime_state().ai_awake = False
    return {"awake": False}


def voice_command(command: str):
    wake()
    return {"command": command, "intent": command.lower().replace(" ", "_")}


def ask_llm(prompt: str):
    wake()
    return {
        "prompt": prompt,
        "response": f"Mission plan for: {prompt}",
        "steps": ["observe", "decide", "act", "report"],
    }


def ask_vlm(question: str):
    wake()
    return {"question": question, "answer": "I can see a person, a traffic light, and open floor space."}


def plan_mission(goal: str):
    wake()
    return {"goal": goal, "plan": ["localize", "navigate", "inspect", "summarize"]}


def summarize_scene():
    wake()
    return "Scene summary: open corridor, one pedestrian, green traffic light, no obstacle inside 0.6m."


def status() -> dict:
    return {"awake": runtime_state().ai_awake}
