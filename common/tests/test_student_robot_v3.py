"""Smoke tests for the teaching-friendly MentorPi API."""

from __future__ import annotations

import sys
from pathlib import Path
import unittest
import os

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "lib"))

if os.environ.get("ROS_DISTRO"):
    from student_robot_v3 import bot  # noqa: E402
else:
    bot = None


@unittest.skipUnless(os.environ.get("ROS_DISTRO"), "Real MentorPi integration tests require a sourced ROS2 environment.")
class StudentRobotV3SmokeTests(unittest.TestCase):
    def setUp(self):
        self.robot = bot()
        self.robot.reset()

    def test_compatibility_namespaces_exist(self):
        for name in ("move", "eyes", "camera", "vision", "voice", "buzzer", "sonar", "infrared", "line"):
            self.assertTrue(hasattr(self.robot, name), name)

    def test_mentorpi_namespaces_exist(self):
        for name in ("lidar", "depth", "slam", "nav", "mediapipe", "yolo", "autodrive", "multi", "ai"):
            self.assertTrue(hasattr(self.robot, name), name)

    def test_navigation_workflow(self):
        self.robot.slam.save_map("test_map")
        started = self.robot.nav.start_navigation("test_map")
        goal = self.robot.nav.go_to(1.0, 2.0, 90.0)
        arrived = self.robot.nav.wait_until_arrived()
        self.assertEqual(started["map_name"], "test_map")
        self.assertEqual(goal["goal"], (1.0, 2.0, 90.0))
        self.assertTrue(arrived["arrived"])

    def test_lidar_and_ai_workflows(self):
        lidar = self.robot.lidar.start_obstacle_avoidance()
        ai = self.robot.ai.ask_llm("Create a patrol route")
        self.assertEqual(lidar["mode"], "obstacle_avoidance")
        self.assertIn("steps", ai)


if __name__ == "__main__":
    unittest.main()
