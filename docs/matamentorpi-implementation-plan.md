# MataMentorPi Implementation Plan

## Goal

Create a `MataMentorPi` lesson/library repo that:

- preserves the beginner-friendly `MataTurboPi` teaching style and compatibility
- includes all current TurboPi-style movement / eyes / camera / voice / vision workflows
- adds MentorPi-specific ROS2 capabilities including lidar, depth camera, SLAM, navigation, MediaPipe, YOLO, autonomous driving, and large-model workflows
- can be packaged into `robot_ops_web`
- can be imported into `robot-classroom`
- can run with a dedicated browser simulator runtime, not only on the physical robot

This document is a preparation spec for implementation.

## Source Audit

### Official MentorPi Sources

- Repo: [Hiwonder/MentorPi](https://github.com/Hiwonder/MentorPi)
- Docs: [MentorPi v2.0 documentation](https://docs.hiwonder.com/projects/MentorPi/en/latest/)
- Branch verified from GitHub on April 1, 2026:
  - `MentorPi-M1`
  - `MentorPi-A1`
  - `MentorPi-T1`

### Existing Local Baselines

- Existing TurboPi lesson/library repo: [/Users/john/Documents/Code/MataTurboPi](/Users/john/Documents/Code/MataTurboPi)
- Existing `robot_ops_web` lesson delivery code: [/Users/john/Documents/Code/robot_ops_web/README.md](/Users/john/Documents/Code/robot_ops_web/README.md)
- Existing `robot-classroom` lesson import/runtime code:
  - [/Users/john/Documents/Code/robot-classroom/backend/services/workspace_service.py](/Users/john/Documents/Code/robot-classroom/backend/services/workspace_service.py)
  - [/Users/john/Documents/Code/robot-classroom/backend/routes/simulator.py](/Users/john/Documents/Code/robot-classroom/backend/routes/simulator.py)
  - [/Users/john/Documents/Code/robot-classroom/deployment/scripts/import_lessons_from_directory.py](/Users/john/Documents/Code/robot-classroom/deployment/scripts/import_lessons_from_directory.py)

## What TurboPi Already Gives Us

Current `MataTurboPi` already provides a clean student-facing API layer in [/Users/john/Documents/Code/MataTurboPi/common/lib](/Users/john/Documents/Code/MataTurboPi/common/lib):

- movement: `forward`, `backward`, `left`, `right`, `turn_left`, `turn_right`, `diagonal_left`, `diagonal_right`, `drift_left`, `drift_right`, `drive_for`, `stop`
- camera servo: `center_all`, `set_pitch`, `set_yaw`, `nod`, `shake`, `wiggle`, `glance_left/right`, `look_up/down`
- RGB eyes
- buzzer / horn / sound
- TTS
- sonar / ultrasonic / infrared
- OpenCV color vision helpers
- line follower / object tracking / QR / avoidance clients
- aggregate robot object: `bot(...)` in [/Users/john/Documents/Code/MataTurboPi/common/lib/student_robot_v2.py](/Users/john/Documents/Code/MataTurboPi/common/lib/student_robot_v2.py)

Current lesson slugs in `MataTurboPi`:

- `lesson01` to `lesson07`
- V2 mirrors: `lesson11` to `lesson17`

This is the compatibility floor for `MataMentorPi`.

## Official MentorPi Lesson Map

From the official docs, MentorPi is organized into these major lesson families:

1. Motion Control Lesson
2. Lidar Lesson
3. Depth Camera Basic Lesson
4. Mapping Lesson
5. Navigation Lesson
6. ROS+OpenCV Lesson
7. MediaPipe Human-robot Interaction
8. Machine Learning
9. Autonomous Driving Lesson
10. Master Slave And Group Control
11. Large AI Model Course

### Lesson-to-Source Mapping

This is the most useful implementation mapping from the official docs plus the repo structure.

| Lesson family | Main docs/examples | Main source packages |
| --- | --- | --- |
| Motion control | mecanum / ackermann speed control, IMU, odom | `driver/controller`, `calibration`, `peripherals` |
| Lidar | obstacle avoidance, following, guarding | `app/app/lidar_controller.py`, `app/launch/lidar_node.launch.py` |
| Depth camera basics | camera setup, ROS topics, point cloud | `peripherals/launch/depth_camera.launch.py`, `ascamera` integration through launch files |
| Mapping | SLAM toolbox, RTAB-Map | `slam/launch/slam.launch.py`, `slam/launch/rtabmap_slam.launch.py` |
| Navigation | Nav2, AMCL, DWA, point-to-point nav | `navigation/launch/navigation.launch.py`, `large_models/navigation_controller.py` |
| ROS + OpenCV | color detection, QR, line following, color tracking, chassis tracking | `example/example/color_detect`, `example/example/qrcode`, `app/app/line_following.py`, `example/example/color_track`, `app/app/object_tracking.py` |
| MediaPipe HRI | fingertip trajectory, hand following, posture, pose | `example/example/hand_trajectory`, `example/example/hand_track`, `example/example/body_control`, `app/app/hand_gesture.py` |
| Machine learning | YOLO training and inference | `yolov5_ros2`, `example/example/yolov5_detect` |
| Autonomous driving | lane keeping, road signs, traffic lights, turning, parking | `example/example/self_driving`, `example/example/yolov5_detect` |
| Multi-robot | master/slave, formation/group control | `multi` |
| Large AI model | voice module, LLM robot control, VLM navigation/tracking | `large_models` |

## MentorPi Repo Package Inventory

The official repo is broader than `MataTurboPi`. These packages matter for `MataMentorPi`:

- `driver/controller`
  - chassis kinematics
  - odom publishing
  - init pose
  - mecanum and ackermann support
- `driver/ros_robot_controller`
  - low-level board, motors, buzzer, RGB, PWM/bus servo access
- `driver/sdk`
  - common math, contour helpers, PID, YAML helpers
- `peripherals`
  - depth camera launch
  - joystick and teleop
  - IMU TF broadcaster
- `calibration`
  - linear and angular calibration tools
- `app`
  - lidar controller
  - line following
  - color/object tracking
  - AR app
  - hand gesture app
  - hand trajectory app
- `example`
  - beginner-facing demos and focused task nodes
- `slam`
  - mapping launch stacks and map save tool
- `navigation`
  - Nav2 launch stack
- `multi`
  - formation and TF follower tools
- `large_models`
  - speech wakeup
  - LLM control
  - VLM camera workflows
  - track-anything with RGB + depth
- `simulations/mentorpi_description`
  - URDF / meshes for ackermann and mecanum variants

## Proposed MataMentorPi API Surface

The cleanest way to keep compatibility is:

1. keep all existing TurboPi-style modules and names where behavior still makes sense
2. add MentorPi-only namespaces instead of forcing students into raw ROS services
3. keep a single aggregate robot object like `bot(...)`

### Proposed top-level modules

- `robot_moves.py`
- `camera_lib.py`
- `eyes_lib.py`
- `buzzer_lib.py`
- `tts_lib.py`
- `vision_lib.py`
- `sonar_lib.py`
- `infrared_lib.py`
- `line_follower_lib.py`
- `tracking_lib.py`
- `qrcode_lib.py`
- `avoidance_lib.py`
- `lidar_lib.py`
- `depth_camera_lib.py`
- `slam_lib.py`
- `navigation_lib.py`
- `mediapipe_lib.py`
- `yolo_lib.py`
- `autodrive_lib.py`
- `multi_robot_lib.py`
- `mentor_ai_lib.py`
- `student_robot_v3.py`

### Compatibility namespaces on `bot(...)`

Keep existing namespaces:

- `move`
- `eyes`
- `camera`
- `vision`
- `voice`
- `buzzer`
- `sonar`
- `infrared`
- `line`
- `tracking`
- `avoidance`
- `qrcode`

Add new MentorPi namespaces:

- `lidar`
- `depth`
- `slam`
- `nav`
- `mediapipe`
- `yolo`
- `autodrive`
- `multi`
- `ai`

### Proposed public functions

These should be our own stable teaching API, even if the underlying ROS nodes differ.

#### `lidar`

- `enter()`
- `exit()`
- `start_obstacle_avoidance(threshold_m=0.6, scan_angle_deg=90, speed=0.2)`
- `start_follow(target_distance_m=0.3, scan_angle_deg=90, speed=0.2)`
- `start_guard(threshold_m=0.6, scan_angle_deg=90, speed=0.2)`
- `set_mode(mode)`
- `set_params(threshold_m, scan_angle_deg, speed)`
- `stop()`
- `scan_snapshot()`

This maps cleanly to `app/app/lidar_controller.py`, which exposes `enter`, `exit`, `set_running`, and `set_param`.

#### `depth`

- `rgb_frame()`
- `depth_frame()`
- `point_cloud_snapshot()`
- `depth_at(x, y)`
- `distance_at(x, y)`
- `camera_info()`
- `start_web_stream()`
- `stop_web_stream()`

This should wrap the `ascamera` topics rather than asking students to subscribe manually.

#### `slam`

- `start_mapping(mode="2d")`
- `stop_mapping()`
- `save_map(name)`
- `start_rtabmap()`
- `stop_rtabmap()`
- `map_status()`

Backed by `slam.launch.py`, `rtabmap_slam.launch.py`, and `slam/slam/map_save.py`.

#### `nav`

- `start_navigation(map_name=None)`
- `set_pose(x, y, yaw_deg)`
- `go_to(x, y, yaw_deg=0)`
- `cancel_goal()`
- `is_busy()`
- `wait_until_arrived(timeout_s=None)`
- `waypoints(points)`

Backed by Nav2 and the `NavigationController` pattern in `large_models/navigation_controller.py`.

#### `mediapipe`

- `detect_hands()`
- `detect_pose()`
- `detect_face()`
- `follow_hand()`
- `finger_trajectory()`
- `body_control()`
- `fall_detection()`

#### `yolo`

- `detect()`
- `detect_signs()`
- `detect_traffic_light()`
- `load_engine(engine_name)`
- `train_dataset(data_yaml, epochs=..., imgsz=...)`

#### `autodrive`

- `lane_follow()`
- `detect_road_sign()`
- `detect_traffic_light()`
- `turn_decision()`
- `auto_park()`
- `run_course()`

These should wrap the `self_driving` and `yolov5_detect` examples into student-safe helpers.

#### `multi`

- `start_leader()`
- `start_follower()`
- `set_formation(name)`
- `broadcast_pose()`
- `follow_tf()`

#### `ai`

- `wake_word(enable=True)`
- `chat(prompt)`
- `control_move(prompt)`
- `visual_patrol(prompt)`
- `color_track(prompt)`
- `camera_query(prompt)`
- `navigate_with_vision(prompt)`
- `track_anything(prompt_or_click)`

## Lesson Plan for MataMentorPi

The best teaching structure is not a direct copy of Hiwonder’s chapter numbering. We should keep the `MataTurboPi` teaching progression and extend it.

### Phase 1: TurboPi-compatible foundation

- `lesson01`: robot movement and demo
- `lesson02`: robot animation / personality
- `lesson03`: color vision
- `lesson04`: sound / camera / RGB expression
- `lesson05`: library test bench
- `lesson06`: project
- `lesson07`: advanced project

### Phase 2: MentorPi sensor and ROS extension

- `lesson08`: lidar basics and safety
- `lesson09`: lidar obstacle avoidance / follow / guard
- `lesson10`: depth camera basics
- `lesson11`: RGB + depth understanding
- `lesson12`: 2D mapping
- `lesson13`: navigation basics
- `lesson14`: color detection / QR / line following
- `lesson15`: object tracking and chassis tracking
- `lesson16`: MediaPipe hand / pose interaction
- `lesson17`: YOLO sign and traffic-light detection
- `lesson18`: autonomous driving
- `lesson19`: multi-robot control
- `lesson20`: AI voice / LLM / VLM projects

### Optional V2/V3 mirrored lessons

If we want the `student_robot_v2` pattern to continue, create:

- `lesson21` to `lesson40` as aggregate-object mirrors

I do not recommend building all mirrored lessons first. We should first ship the primary lesson set and only mirror the lessons that actually need the simplified `bot(...)` teaching path.

## Suggested Repo Layout for MataMentorPi

```text
MataMentorPi/
  common/
    lib/
      robot_moves.py
      camera_lib.py
      eyes_lib.py
      buzzer_lib.py
      tts_lib.py
      vision_lib.py
      sonar_lib.py
      infrared_lib.py
      line_follower_lib.py
      tracking_lib.py
      qrcode_lib.py
      avoidance_lib.py
      lidar_lib.py
      depth_camera_lib.py
      slam_lib.py
      navigation_lib.py
      mediapipe_lib.py
      yolo_lib.py
      autodrive_lib.py
      multi_robot_lib.py
      mentor_ai_lib.py
      student_robot_v3.py
  lessons/
    lesson01/
    ...
    lesson20/
    lib/
  simulator/
    core/
    shims/
    courses/
    scenes/
```

## Simulator Requirements

`robot-classroom` currently hardcodes the bundled simulator runtime to `runtime/mataturbopi/simulator` in:

- [/Users/john/Documents/Code/robot-classroom/backend/services/workspace_service.py](/Users/john/Documents/Code/robot-classroom/backend/services/workspace_service.py)
- [/Users/john/Documents/Code/robot-classroom/backend/routes/simulator.py](/Users/john/Documents/Code/robot-classroom/backend/routes/simulator.py)

### What must change

1. make simulator runtime selection depend on `lesson.robot_type`
2. add a new bundled runtime:
   - `runtime/matamentorpi/simulator`
3. make the simulator route load the correct course directory for the selected robot type
4. make workspace materialization copy the correct simulator runtime for the lesson’s robot type

### Minimum MataMentorPi simulator state additions

TurboPi simulator state currently models:

- robot pose
- eyes
- camera servo
- sonar
- speech / buzzer / horn
- obstacle course

MentorPi simulator needs additional state for:

- lidar scan sectors or synthetic scan samples
- depth camera synthetic frame
- point cloud summary
- map grid / SLAM state
- navigation goal and path
- line-following lane geometry
- YOLO detections / traffic lights / road signs
- hand / body / pose synthetic targets
- multi-robot ghosts or partner robots

### Minimum simulator shim additions

We will need simulator shims for:

- `lidar_lib.py`
- `depth_camera_lib.py`
- `slam_lib.py`
- `navigation_lib.py`
- `mediapipe_lib.py`
- `yolo_lib.py`
- `autodrive_lib.py`
- `multi_robot_lib.py`
- `mentor_ai_lib.py`

The simulator should not try to emulate full ROS2 internals. It should emulate student-observable outcomes.

## robot_classroom Requirements

`robot-classroom` is already close to supporting a new robot type because lesson import is robot-type based.

### Good news

- lesson metadata already includes `robot_type`
- import scripts already support `--robot-type`
- classroom filtering already supports robot families

### Required changes

1. add `matamentorpi` lesson sync/import flow
2. make workspace support-tree selection robot-type aware
3. make bundled simulator root robot-type aware
4. add `runtime/matamentorpi/simulator`
5. ensure classroom home and simulator launch pass through `robot_type` consistently

## robot_ops_web Requirements

`robot_ops_web` mainly packages and serves lesson bundles to robots.

### Required changes

1. support a `matamentorpi` lesson source directory alongside existing TurboPi content
2. ensure bundle build includes:
   - `lessons/`
   - `common/`
   - optionally `simulator/` if we want robot-side parity
3. expose MentorPi robot type through admin/config selection
4. ensure lesson selection payloads keep:
   - `lesson_id`
   - `level_id`
   - `lesson_path`
   - `entry`
5. keep robot-side workspace materialization compatible with richer common libraries

## Recommended Implementation Order

### Stage 1: bootstrap the repo

- create `MataMentorPi` from `MataTurboPi`
- preserve current compatible modules
- add empty MentorPi-specific modules with stable public APIs
- keep imports notebook-friendly

### Stage 2: get lesson delivery working

- create initial `lesson.json` files
- import `matamentorpi` into `robot-classroom`
- update `robot_ops_web` to serve the new robot type

### Stage 3: ship simulator-first wrappers

- implement simulator shims first for:
  - `lidar_lib`
  - `depth_camera_lib`
  - `navigation_lib`
  - `slam_lib`
- this lets us build lessons before the full hardware wrappers are polished

### Stage 4: ship physical robot wrappers

- wrap official ROS services/topics from MentorPi packages
- normalize them into our stable student API

### Stage 5: add advanced lessons

- MediaPipe
- YOLO
- autonomous driving
- multi-robot
- AI model workflows

## Recommended First Deliverable

The fastest path to value is:

1. create `MataMentorPi` repo skeleton from `MataTurboPi`
2. ship lessons `01` to `10`
3. add `matamentorpi` support to `robot-classroom`
4. add a minimal MentorPi simulator with:
   - motion
   - lidar
   - depth distance sampling
   - mapping/navigation placeholders
5. only then expand into autonomous driving and AI lessons

## Open Decisions

These need to be decided before implementation gets too far:

1. Do we want one MentorPi profile or separate profiles for `M1`, `A1`, and `T1`?
2. Do we keep lesson numbering continuous from TurboPi style, or mirror Hiwonder chapter numbering?
3. Do we want `student_robot_v3` immediately, or only after the raw module APIs are stable?
4. How realistic does the simulator need to be for SLAM/navigation:
   - lesson-friendly fake outcomes
   - or a more geometric map/path simulator

## Recommendation

My recommendation is:

- define `matamentorpi` as one robot family first
- target `MentorPi-M1` behavior first
- keep the TurboPi-compatible lesson style
- add MentorPi features through new namespaces, not by changing old ones
- build simulator support around learning outcomes rather than full ROS fidelity

That gives us the best chance of shipping a usable classroom system quickly without breaking the simplicity that makes `MataTurboPi` work well for students.
