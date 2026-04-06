# Lesson 11: Map Saving and Localization

Focus: prepare MentorPi to reuse a saved map instead of rebuilding it every run.

Official MentorPi mapping: saved-map flow, AMCL-style localization, and navigation setup lessons.

Student goals:
- save a clean map name
- set the robot pose on that map
- explain how localization supports navigation

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
myRobot.slam.save_map("library_room")
myRobot.nav.start_navigation(map_name="library_room")
print(myRobot.nav.set_pose(1.2, 0.4, 90))
```

Build challenge: choose good spawn points for three starting areas.
