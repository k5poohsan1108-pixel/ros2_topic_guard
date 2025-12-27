#!/bin/bash

# ROS 2 ワークスペースに移動
cd ~/ros2_ws

# ビルドして環境をセット
colcon build
source install/setup.bash

# 5秒だけ Launch を走らせてログに保存
timeout 5 ros2 launch ros2_topic_guard battery_monitor_launch.py > /tmp/battery_monitor.log

# Battery Publisher の出力確認
grep "Battery:" /tmp/battery_monitor.log
if [ $? -ne 0 ]; then
  echo "FAIL: No Battery messages"
  exit 1
fi

# Battery Checker の OK 出力確認
grep "Battery OK:" /tmp/battery_monitor.log
if [ $? -ne 0 ]; then
  echo "WARNING: No OK logs"
fi

echo "Battery monitor basic output OK"
