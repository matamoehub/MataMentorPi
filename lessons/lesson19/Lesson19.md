# Lesson 19: Vision Language Robot Assistant

Focus: combine perception with explanation.

Official MentorPi mapping: VLM tracking, scene understanding, and camera-language workflows in the large-model package.

Student goals:
- ask a visual question
- summarize a scene
- connect scene understanding to navigation decisions

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
print(myRobot.ai.ask_vlm("What is in front of the robot?"))
print(myRobot.ai.summarize_scene())
```

Build challenge: create a robot announcer that describes what it sees before moving.
