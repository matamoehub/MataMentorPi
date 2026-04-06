# Lesson 2: Eyes, Camera, Voice, and Sound

Focus: give MentorPi personality with `eyes`, `camera`, `voice`, and `buzzer`.

Official MentorPi mapping: low-level robot controller peripherals and expression-style demos.

Student goals:
- change both eye colors
- look left and right with the camera
- make the robot speak and beep

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
myRobot.eyes.color(0, 80, 255)
myRobot.camera.nod()
myRobot.voice.say("Hello, I am MentorPi.")
myRobot.buzzer.celebrate()
```

Build challenge: create a short robot introduction routine.
