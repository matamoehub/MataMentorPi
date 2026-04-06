# MataMentorPi
<<<<<<< HEAD
Mentor Pi Library and lessons 
=======

`MataMentorPi` is a teaching-friendly robotics library and lesson repo built around Hiwonder MentorPi, using the approachable V2-style student API pattern from TurboPi.

What this repo now includes:

- a V2 aggregate `bot()` object in [`common/lib/student_robot_v3.py`](/Users/john/Documents/Code/MataMentorPi/common/lib/student_robot_v3.py)
- compatibility-style modules for movement, camera, eyes, buzzer, speech, sonar, infrared, vision, line following, tracking, QR, and avoidance
- MentorPi-native modules for lidar, depth camera, SLAM, navigation, MediaPipe, YOLO, autonomous driving, multi-robot control, and AI workflows
- a 20-lesson progression in [`lessons/`](/Users/john/Documents/Code/MataMentorPi/lessons) with special MentorPi capability lessons

Integration policy:

- libraries now prefer real ROS2 topics, services, and launch files from the official MentorPi stack
- mock classroom returns were removed from the main MentorPi-facing modules
- where the public Hiwonder repo does not expose a standalone interface, the library raises a clear integration error instead of faking data

Reference alignment:

- official Hiwonder MentorPi GitHub repo and docs for package and lesson-family mapping
- local TurboPi V2 codebase for student-facing API style and lesson progression guidance

The source audit and design notes are in [docs/matamentorpi-implementation-plan.md](/Users/john/Documents/Code/MataMentorPi/docs/matamentorpi-implementation-plan.md).

A TurboPi-to-MentorPi comparison and lesson-family mapping is in [docs/turbopi-mentorpi-comparison.md](/Users/john/Documents/Code/MataMentorPi/docs/turbopi-mentorpi-comparison.md).

A module-by-module source mapping to the official Hiwonder repo is in [docs/mentorpi-source-map.md](/Users/john/Documents/Code/MataMentorPi/docs/mentorpi-source-map.md).
