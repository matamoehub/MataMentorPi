# Lesson 13: MediaPipe Hands

Focus: use hand information as an input device for the robot.

Official MentorPi mapping: hand tracking, fingertip trajectory, and gesture app examples.

Student goals:
- detect a hand
- follow hand position
- record a fingertip path

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
print(myRobot.mediapipe.detect_hands())
print(myRobot.mediapipe.follow_hand())
print(myRobot.mediapipe.finger_trajectory())
```

Build challenge: map a hand gesture to a movement command.
