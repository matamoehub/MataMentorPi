# Lesson 14: Pose and Gesture Control

Focus: turn full-body information into robot responses.

Official MentorPi mapping: body control, pose interaction, and fall-detection style demos.

Student goals:
- detect body pose
- trigger robot behavior from pose states
- discuss fall detection and safety responses

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
print(myRobot.mediapipe.detect_pose())
print(myRobot.mediapipe.body_control())
print(myRobot.mediapipe.fall_detection())
```

Build challenge: create a no-touch start signal for a classroom demo.
