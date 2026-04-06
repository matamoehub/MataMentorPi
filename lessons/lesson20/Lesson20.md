# Lesson 20: MentorPi Capstone Missions

Focus: combine MentorPi's unique capabilities into one end-to-end project.

Official MentorPi mapping: mapping, navigation, perception, and AI lesson families working together.

Student goals:
- choose a mission theme
- combine at least three MentorPi-only modules
- explain sensing, decision, and action in one workflow

Suggested capstones:
- map a room, navigate to waypoints, and describe the scene at each stop
- follow a hand gesture to start a delivery mission
- detect a traffic light, then drive and park

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
myRobot.slam.start_mapping()
myRobot.slam.save_map("capstone_map")
myRobot.nav.start_navigation("capstone_map")
print(myRobot.ai.plan_mission("Inspect the room and report hazards"))
```

Build challenge: write your own final mission brief and demo checklist.
