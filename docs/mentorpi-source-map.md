# MentorPi Source Map

This file maps the local `MataMentorPi` teaching API to the official Hiwonder MentorPi repository structure.

Official source root:

- [Hiwonder/MentorPi](https://github.com/Hiwonder/MentorPi)

Verified package layout from the current public repo:

- `app`
- `bringup`
- `calibration`
- `driver`
- `example`
- `interfaces`
- `large_models`
- `large_models_msgs`
- `multi`
- `navigation`
- `peripherals`
- `simulations/mentorpi_description`
- `slam`
- `yolov5_ros2`

## Local API to Official Package Mapping

| Local module | Purpose in MataMentorPi | Official MentorPi package(s) |
| --- | --- | --- |
| `robot_moves.py` | teaching-friendly movement API | `driver`, `bringup`, `calibration` |
| `camera_lib.py` | camera servo gestures | `driver`, `peripherals` |
| `eyes_lib.py` | RGB eye state helpers | `driver/ros_robot_controller` |
| `buzzer_lib.py` | buzzer and sound patterns | `driver/ros_robot_controller` |
| `tts_lib.py` | speech-style helper layer | `large_models`, voice module workflows |
| `vision_lib.py` | color and image helpers | `example`, `app` |
| `line_follower_lib.py` | line-following logic | `app/app/line_following.py`, `example` |
| `tracking_lib.py` | color and object tracking | `app/app/object_tracking.py`, `example/example/color_track` |
| `qrcode_lib.py` | QR scan activities | `example/example/qrcode` |
| `avoidance_lib.py` | reactive close-range avoidance | `app`, sensor controller flows |
| `lidar_lib.py` | lidar modes and scan snapshots | `app`, lidar launch and controller |
| `depth_camera_lib.py` | RGB, depth, point cloud wrappers | `peripherals`, depth camera launch |
| `slam_lib.py` | mapping helpers | `slam` |
| `navigation_lib.py` | goal and waypoint helpers | `navigation`, `large_models/navigation_controller.py` |
| `mediapipe_lib.py` | hand, pose, gesture lessons | `example`, `app/app/hand_gesture.py` |
| `yolo_lib.py` | object-detection lessons | `yolov5_ros2`, detection examples |
| `autodrive_lib.py` | self-driving patterns | `example/example/self_driving`, `yolov5_ros2` |
| `multi_robot_lib.py` | team and formation helpers | `multi` |
| `mentor_ai_lib.py` | voice, LLM, VLM abstractions | `large_models`, `large_models_msgs` |

## Lesson Family to Official Package Mapping

| MataMentorPi lesson range | Main theme | Official package family |
| --- | --- | --- |
| 1-5 | TurboPi-style compatibility and reactive robotics | `driver`, `example`, `app` |
| 6-7 | lidar lessons | `app`, lidar launch |
| 8-9 | depth perception | `peripherals`, depth camera stack |
| 10-11 | mapping and localization | `slam` |
| 12 | navigation | `navigation`, `large_models` |
| 13-14 | MediaPipe HRI | `example`, `app` |
| 15 | machine learning | `yolov5_ros2` |
| 16 | autonomous driving | `example`, `yolov5_ros2` |
| 17 | group control | `multi` |
| 18-20 | large-model workflows and capstones | `large_models` |

## Next Integration Step

The current local code intentionally behaves as a stable classroom API and simulator-friendly wrapper layer. The next step is to replace selected mock returns with real ROS2 topic, service, and action adapters that point into the official package launch and runtime nodes.
