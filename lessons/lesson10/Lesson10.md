# Lesson 10: SLAM Mapping

Focus: understand mapping state and map creation workflow.

Official MentorPi mapping: `slam.launch.py`, SLAM Toolbox, and the mapping lesson family in the official docs.

Student goals:
- start mapping
- describe the difference between mapping and navigation
- save a map name for later use

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
print(myRobot.slam.start_mapping())
print(myRobot.slam.save_map("classroom_map"))
print(myRobot.slam.map_status())
```

Build challenge: create a mapping checklist students should follow on a real robot.
