# Lesson 7: Lidar Follow and Guard

Focus: use MentorPi-specific lidar behaviors that go beyond simple avoidance.

Official MentorPi mapping: person-following and guard-style lidar modes from the official app layer.

Student goals:
- switch among lidar modes
- compare follow distance and guard threshold
- explain when each mode is useful

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
print(myRobot.lidar.start_follow(target_distance_m=0.35))
print(myRobot.lidar.start_guard(threshold_m=0.5))
print(myRobot.lidar.scan_snapshot(samples=11))
```

Build challenge: design a museum guard robot routine.
