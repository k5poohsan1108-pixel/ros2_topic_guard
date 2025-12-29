#!/bin/bash
# SPDX-FileCopyrightText: 2025 Keigo Yamaguchi
# SPDX-License-Identifier: GPL-3.0-only

set -e

cd /root/ros2_ws
source install/setup.bash

ros2 launch ros2_topic_guard battery_monitor_launch.py &
PID=$!

sleep 5
kill $PID || true

echo "Launch test completed"
