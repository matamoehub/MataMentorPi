# Lesson 8: Depth Camera Basics

Focus: inspect RGB and depth data from MentorPi's depth camera pipeline.

Official MentorPi mapping: depth camera launch and introductory depth-camera lessons.

Student goals:
- compare RGB and depth frames
- read distance at a pixel
- start and stop a stream

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
print(myRobot.depth.rgb_frame())
print(myRobot.depth.depth_frame())
print(myRobot.depth.distance_at(2, 1))
myRobot.depth.start_web_stream()
```

Build challenge: find the closest point in a small depth matrix.
