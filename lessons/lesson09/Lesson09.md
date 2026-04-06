# Lesson 9: Point Clouds and Spatial Decisions

Focus: move from a single depth number to a small 3D understanding of space.

Official MentorPi mapping: point cloud and RTAB-Map preparation ideas from the depth and mapping lesson families.

Student goals:
- capture a point cloud snapshot
- estimate free space in front of the robot
- choose between forward, left, or right movement

Starter code:
```python
from student_robot_v3 import bot

myRobot = bot()
cloud = myRobot.depth.point_cloud_snapshot()
print(cloud[:5])
center_distance = myRobot.depth.distance_at(3, 2)
print("Center distance:", center_distance)
```

Build challenge: write a free-space chooser for a doorway.
