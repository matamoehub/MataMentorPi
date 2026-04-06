# Lesson 4: Color Vision and QR Codes

Focus: use the camera as a sensor, not just a viewer.

Official MentorPi mapping: ROS plus OpenCV examples for color detection and QR scanning.

Student goals:
- capture an image snapshot
- detect a color blob
- scan a QR code and trigger an action

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
print(myRobot.vision.capture(show=False))
print(myRobot.vision.detect_color("green"))
code = myRobot.qrcode.scan()
print("QR:", code)
```

Build challenge: drive to a station based on a QR code string.
