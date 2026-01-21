# ros2_topic_guard
[![test](https://github.com/k5poohsan1108-pixel/ros2_topic_guard/actions/workflows/test.yml/badge.svg)](https://github.com/k5poohsan1108-pixel/ros2_topic_guard/actions/workflows/test.yml)

`ros2_topic_guard` は、ROS 2 においてトピックの内容を監視するためのパッケージであり、
本課題ではバッテリー残量トピックの監視を対象としている。

---

本パッケージは、以下の 2 つのノードから構成される。

- `battery_publisher` : バッテリー残量を模擬した数値を定期的に publish するノード
- `battery_checker` : バッテリー残量トピックを subscribe し、残量に応じた状態をトピックとして publish するノード

---

使用するトピックは以下の通りである。

- `battery_level`（`std_msgs/msg/Float32`）  
  バッテリー残量（%）を表すトピック
- `battery_state`（`std_msgs/msg/Int8`）  
  バッテリー状態を表すトピック  
  （0: 正常, 1: 注意, 2: 危険）

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

## 使用環境

- Ubuntu 22.04
- ROS 2 Humble
  
## ライセンス

- このソフトウェアのパッケージは、GNU 一般公衆利用許諾書 第3版（GPL-3.0-only）の下で公開されている。
- Copyright (c) 2025 Keigo Yamaguchi


