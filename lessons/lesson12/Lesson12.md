# Lesson 12: Navigation Goals and Waypoints

Focus: move from mapping to mission execution with point-to-point navigation.

Official MentorPi mapping: navigation launch files and `navigation_controller.py` style goal control.

Student goals:
- start navigation on a saved map
- send a single goal
- queue and finish waypoint missions

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
myRobot.nav.start_navigation("library_room")
print(myRobot.nav.go_to(2.0, 1.0, 0))
print(myRobot.nav.waypoints([(2.0, 1.0, 0), (2.5, 1.4, 90)]))
print(myRobot.nav.wait_until_arrived())
```

Build challenge: create a delivery route with three stops.
