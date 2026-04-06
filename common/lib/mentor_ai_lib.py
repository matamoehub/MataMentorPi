"""Real large-model helpers backed by MentorPi agent_process, TTS, and VLLM services."""

from __future__ import annotations

import os

from _mentorpi_ros import MentorPiIntegrationError, call_service, publish_text, start_launch, wait_for_message

__version__ = "3.0.0"


def _api_key() -> str:
    value = os.environ.get("OPENAI_API_KEY") or os.environ.get("MENTORPI_OPENAI_API_KEY")
    if not value:
        raise MentorPiIntegrationError("OPENAI_API_KEY is required for the official MentorPi large_models agent_process.")
    return value


def _base_url() -> str:
    return os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")


def wake():
    start_launch("mentorpi_voice", "large_models", "start.launch.py")
    return {"awake": True}


def sleep():
    return {"awake": False}


def voice_command(command: str):
    wake()
    publish_text("tts_node/tts_text", command)
    return {"command": command}


def ask_llm(prompt: str):
    wake()
    result = call_service(
        "agent_process/set_llm_content",
        "large_models_msgs.srv",
        "SetContent",
        lambda req: (
            setattr(req, "model", os.environ.get("MENTORPI_LLM_MODEL", "gpt-4o-mini")),
            setattr(req, "api_key", _api_key()),
            setattr(req, "base_url", _base_url()),
            setattr(req, "prompt", "You are MentorPi's planning assistant."),
            setattr(req, "query", prompt),
        ),
        timeout=30.0,
    )
    return {"prompt": prompt, "response": result.message}


def ask_vlm(question: str):
    wake()
    result = call_service(
        "agent_process/set_vllm_content",
        "large_models_msgs.srv",
        "SetContent",
        lambda req: (
            setattr(req, "model", os.environ.get("MENTORPI_VLM_MODEL", "gpt-4o-mini")),
            setattr(req, "api_key", _api_key()),
            setattr(req, "base_url", _base_url()),
            setattr(req, "prompt", "Answer briefly based on the current robot camera frame."),
            setattr(req, "query", question),
        ),
        timeout=30.0,
    )
    return {"question": question, "answer": result.message}


def plan_mission(goal: str):
    return ask_llm(goal)


def summarize_scene():
    return ask_vlm("Summarize the current scene for the operator.")


def status() -> dict:
    return {"llm_service": "agent_process/set_llm_content", "vlm_service": "agent_process/set_vllm_content"}
