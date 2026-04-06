# Lesson 15: YOLO Object Detection

Focus: use machine-learning detection to recognize objects of interest.

Official MentorPi mapping: `yolov5_ros2` and object-detection examples from the official repo.

Student goals:
- load a model name
- inspect detection results
- choose a response based on the strongest detection

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
myRobot.yolo.load_model("yolov5s")
print(myRobot.yolo.detect())
print(myRobot.yolo.highest_confidence())
```

Build challenge: stop at a traffic light but continue for a person.
