#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Keigo Yamaguchi
# SPDX-License-Identifier: GPL-3.0-only

import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='ros2_topic_guard',
            executable='battery_publisher',
            name='battery_publisher',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='ros2_topic_guard',
            executable='battery_checker',
            name='battery_checker',
            output='screen',
            parameters=[{'threshold': 50.0}]
        ),
    ])
