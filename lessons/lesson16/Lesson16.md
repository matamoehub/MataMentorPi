# Lesson 16: Autonomous Driving

Focus: connect lane, sign, and turning logic into a road-driving workflow.

Official MentorPi mapping: self-driving examples, traffic-light detection, turning, and parking lessons.

Student goals:
- inspect lane status
- react to a traffic light
- plan a turn or parking sequence

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
print(myRobot.autodrive.lane_status())
print(myRobot.autodrive.detect_traffic_light())
print(myRobot.autodrive.plan_turn("right"))
print(myRobot.autodrive.parking_sequence())
```

Build challenge: design a mini street course for classroom testing.
