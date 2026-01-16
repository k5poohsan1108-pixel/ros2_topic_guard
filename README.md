# ros2_topic_guard
[![test](https://github.com/k5poohsan1108-pixel/ros2_topic_guard/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/k5poohsan1108-pixel/ros2_topic_guard/actions/workflows/test.yml)

ros2_topic_guard は、ROS 2 上で数値トピックを監視し、
その値に基づいた状態を別のトピックとして出力するパッケージである。
本パッケージでは、/battery_level を入力とし、
バッテリー残量に応じた状態を /battery_state として出力する。

---

## 使用環境

- Ubuntu 22.04
- ROS 2 Humble

---

本パッケージは、以下の 2 つのノードから構成される。

- battery_publisher
バッテリー残量を模擬した数値を定期的に publish するノード

- battery_checker
バッテリー残量トピックを subscribe し、残量に応じた状態をトピックとして publish するノード

---

## トピック
- /battery_level（std_msgs/msg/Float32）  
  バッテリー残量（%）
- /battery_state（std_msgs/msg/Int8）  
  バッテリー状態（0: 正常, 1: 注意, 2: 危険）
  
---

以下のコマンドでノード群を起動できる。
```bash
ros2 launch ros2_topic_guard battery_monitor_launch.py
```
別のターミナルで、状態がトピックとして出力される。
```bash
ros2 topic echo /battery_state
 data: 0
```
---

## License

- このソフトウェアのパッケージは、3条項BSDライセンスの下、再頒布および使用が許可される。
- Copyright (c) 2025 Keigo Yamaguchi


