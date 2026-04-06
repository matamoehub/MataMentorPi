# Lesson 1: Movement and Safety

Focus: learn the `bot()` object and the movement namespace in the same friendly V2 style used by TurboPi.

Official MentorPi mapping: motion control lessons and controller basics from the Hiwonder MentorPi repo.

Student goals:
- create a robot object
- drive forward, backward, strafe, and turn
- stop safely and inspect pose updates

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
myRobot.move.forward(seconds=1.0)
myRobot.move.left(seconds=0.8)
myRobot.move.turn_left(seconds=0.5)
print(myRobot.move.pose())
myRobot.stop()
```

Build challenge: drive a square, then report the final pose.
