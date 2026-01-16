#!/bin/bash
# SPDX-FileCopyrightText: 2025 Keigo Yamaguchi
# SPDX-License-Identifier: GPL-3.0-only
set -e

source /opt/ros/humble/setup.bash
source install/setup.bash

ros2 launch ros2_topic_guard battery_monitor_launch.py &
PID=$!

sleep 3

if ros2 topic echo /battery_state --once > /dev/null; then
  echo "battery_state received"
else
  echo "battery_state not received"
  kill $PID
  exit 1
fi

kill $PID


