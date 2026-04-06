# Lesson 6: Lidar Obstacle Avoidance

Focus: begin MentorPi's lidar lesson family with scans and avoidance mode.

Official MentorPi mapping: `app/app/lidar_controller.py` and the lidar launch workflow in the Hiwonder MentorPi repo.

Student goals:
- inspect a lidar scan snapshot
- tune threshold, scan angle, and speed
- start and stop obstacle avoidance mode

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
print(myRobot.lidar.scan_snapshot())
myRobot.lidar.start_obstacle_avoidance(threshold_m=0.7, scan_angle_deg=120, speed=0.25)
print(myRobot.lidar.status())
myRobot.lidar.stop()
```

Build challenge: compare narrow and wide scan angles in a hallway.
