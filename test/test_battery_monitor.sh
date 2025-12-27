#!/bin/bash
set -e

cd /root/ros2_ws

colcon build --packages-select ros2_topic_guard
source install/setup.bash

# Launch を5秒実行
timeout 5 ros2 launch ros2_topic_guard battery_monitor_launch.py > /tmp/battery_monitor.log 2>&1

# publisher が動いたか
grep -q "Battery:" /tmp/battery_monitor.log
echo "Battery publisher OK"

# checker が動いたか
grep -q "Battery" /tmp/battery_monitor.log
echo "Battery checker OK"

# 異常 or 正常のどちらかは出ているか
grep -Eq "Battery OK:|Battery WARNING:" /tmp/battery_monitor.log
echo "Battery judgment OK"
