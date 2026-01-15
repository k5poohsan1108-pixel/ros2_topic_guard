#!/bin/bash
# SPDX-FileCopyrightText: 2025 Keigo Yamaguchi
# SPDX-License-Identifier: GPL-3.0-only

set -e

source /opt/ros/humble/setup.bash
source install/setup.bash

ros2 launch ros2_topic_guard battery_monitor_launch.py &
LAUNCH_PID=$!

sleep 5

STATE=$(ros2 topic echo /battery_state --once | grep data | awk '{print $2}')

kill $LAUNCH_PID || true

if [ "$STATE" = "0" ] || [ "$STATE" = "1" ] || [ "$STATE" = "2" ]; then
  echo "battery_state received: $STATE"
  exit 0
else
  echo "battery_state not received"
  exit 1
fi
