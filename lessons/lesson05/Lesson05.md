# Lesson 5: Tracking and Line Following

Focus: combine multiple simple sensors into a behavior loop.

Official MentorPi mapping: line following, object tracking, and controller apps.

Student goals:
- read the line pattern
- follow a target color
- switch to avoidance if the path is blocked

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
print(myRobot.line.follow_line_step())
myRobot.tracking.start("red ball")
print(myRobot.tracking.step())
print(myRobot.avoidance.start(threshold_m=0.4))
```

Build challenge: design a robot that follows a line until it sees an obstacle.
