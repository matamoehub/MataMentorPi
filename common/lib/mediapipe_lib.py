"""Real MediaPipe and gesture-control adapters for MentorPi."""

from __future__ import annotations

from _mentorpi_ros import call_service, current_image, start_launch

__version__ = "3.0.0"


def detect_hands():
    start_launch("mediapipe_hand", "example", "hand_track/hand_track_node.launch.py")
    return {"image_shape": tuple(current_image().shape), "note": "Use the official hand_track node output on the robot for live detections."}


def detect_pose():
    start_launch("mediapipe_pose", "example", "body_control/body_control.launch.py")
    return {"image_shape": tuple(current_image().shape), "note": "Pose detection is provided by the official body_control launch."}


def detect_face():
    start_launch("mediapipe_face", "example", "mediapipe_example/face_detect.py")
    return {"image_shape": tuple(current_image().shape), "note": "Face detection uses the official mediapipe examples."}


def follow_hand():
    start_launch("hand_gesture", "app", "hand_gesture_node.launch.py")
    call_service("hand_gesture/enter", "std_srvs.srv", "Trigger")
    call_service("hand_gesture/set_running", "std_srvs.srv", "SetBool", lambda req: setattr(req, "data", True))
    return {"running": True, "service": "hand_gesture/set_running"}


def finger_trajectory():
    start_launch("hand_trajectory", "example", "hand_trajectory/hand_trajectory_node.launch.py")
    return {"launch": "hand_trajectory/hand_trajectory_node.launch.py"}


def body_control():
    start_launch("body_control", "example", "body_control/body_control.launch.py")
    return {"launch": "body_control/body_control.launch.py"}


def fall_detection():
    start_launch("fall_detection", "example", "body_control/fall_down_detect.launch.py")
    return {"launch": "body_control/fall_down_detect.launch.py"}


def status() -> dict:
    return {"camera_topic": "/ascamera/camera_publisher/rgb0/image"}
