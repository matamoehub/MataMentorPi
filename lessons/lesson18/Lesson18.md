# Lesson 18: Voice and LLM Missions

Focus: translate spoken goals into higher-level robot plans.

Official MentorPi mapping: speech wakeup, LLM control, and large-model lesson material.

Student goals:
- wake the AI system
- send a voice-style command
- inspect an LLM mission plan

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
print(myRobot.ai.wake())
print(myRobot.ai.voice_command("Go to the desk and report what you find"))
print(myRobot.ai.ask_llm("Create a patrol mission for the lab"))
```

Build challenge: write a prompt that produces a safe robot mission plan.
