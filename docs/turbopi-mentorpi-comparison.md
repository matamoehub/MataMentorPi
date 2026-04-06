# TurboPi to MentorPi Comparison

This document compares the local `MataTurboPi` baseline with the official Hiwonder MentorPi lesson families so `MataMentorPi` stays familiar for students while exposing the extra MentorPi capabilities.

## What We Reused From TurboPi

The local TurboPi repo provides the teaching pattern that students already know:

- one aggregate robot object
- flat, friendly namespaces such as `move`, `eyes`, `camera`, and `voice`
- simple lesson progression from robot basics toward integrated projects
- lesson-side helper modules in `lessons/lib`

That compatibility layer is now preserved in:

- [`common/lib/student_robot_v3.py`](/Users/john/Documents/Code/MataMentorPi/common/lib/student_robot_v3.py)
- [`lessons/lib/student_robot_v3.py`](/Users/john/Documents/Code/MataMentorPi/lessons/lib/student_robot_v3.py)

## What MentorPi Adds

The official Hiwonder MentorPi docs and repo add lesson families that do not exist in TurboPi:

- lidar lessons
- depth camera basics
- 2D and 3D mapping
- autonomous navigation
- MediaPipe human-robot interaction
- YOLO and machine learning
- autonomous driving
- master-slave and group control
- large-model workflows

Primary sources:

- [MentorPi v2.0 docs](https://docs.hiwonder.com/projects/MentorPi/en/latest/index.html)
- [Hiwonder MentorPi GitHub](https://github.com/Hiwonder/MentorPi)

## MataMentorPi Mapping

| TurboPi teaching pattern | MentorPi capability source | MataMentorPi result |
| --- | --- | --- |
| `move`, `eyes`, `camera`, `voice` | motion control and peripherals | compatibility namespaces kept |
| OpenCV color lessons | ROS+OpenCV lessons | `vision`, `tracking`, `qrcode`, `line`, `avoidance` |
| V2 aggregate object | broader MentorPi package layout | `bot()` in `student_robot_v3.py` |
| simple projects | lidar, depth, SLAM, nav, AI courses | new namespaces and capstone lessons |

## Lesson Coverage

| Official MentorPi family | MataMentorPi lessons |
| --- | --- |
| Motion Control Lesson | 1-5 |
| Lidar Lesson | 6-7 |
| Depth Camera Basic Lesson | 8-9 |
| Mapping Lesson | 10-11 |
| Navigation Lesson | 12 |
| ROS+OpenCV Lesson | 4-5 |
| MediaPipe Human-robot Interaction | 13-14 |
| Machine Learning | 15 |
| Autonomous Driving Lesson | 16 |
| Master Slave And Group Control | 17 |
| Large AI Model Course | 18-20 |

## Remaining Next Step

The current repo now mirrors the lesson and API shape well, but the wrappers are still simulator-friendly teaching layers. The next implementation step would be connecting each public helper to the real ROS2 launch files, topics, services, and actions from the official MentorPi packages.
