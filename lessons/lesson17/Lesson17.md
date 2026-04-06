# Lesson 17: Multi-Robot Coordination

Focus: use MentorPi's multi-robot ideas for group behaviors.

Official MentorPi mapping: the `multi` package and master-slave or formation control lessons.

Student goals:
- create a robot team
- assign a leader
- describe a formation

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
print(myRobot.multi.create_team(["mentorpi-1", "mentorpi-2", "mentorpi-3"]))
print(myRobot.multi.assign_leader("mentorpi-2"))
print(myRobot.multi.formation("triangle"))
```

Build challenge: plan a three-robot patrol route.
