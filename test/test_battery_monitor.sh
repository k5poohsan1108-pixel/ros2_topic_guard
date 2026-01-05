#!/bin/bash
# SPDX-FileCopyrightText: 2025 Keigo Yamaguchi
# SPDX-License-Identifier: GPL-3.0-only

set -e

source /root/ros2_ws/install/setup.bash

ros2 launch ros2_topic_guard battery_monitor_launch.py &
PID=$!

sleep 5
kill $PID || true

ros2 topic echo /battery_state -n 1 > /tmp/battery_state.log

grep -E "data: [0-2]" /tmp/battery_state.log

echo "Battery monitor test passed"
