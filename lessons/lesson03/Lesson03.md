# Lesson 3: Sonar and Infrared Sensing

Focus: read close-range sensors before moving.

Official MentorPi mapping: introductory sensing and reactive control patterns.

Student goals:
- measure distance with sonar
- inspect left, center, and right infrared states
- decide whether the path is safe

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
print(myRobot.sonar.distance())
print(myRobot.infrared.read())
if myRobot.sonar.is_clear(0.5):
    myRobot.move.forward(0.6)
else:
    myRobot.move.turn_left(0.4)
```

Build challenge: stop when an obstacle is too close, then turn away.
