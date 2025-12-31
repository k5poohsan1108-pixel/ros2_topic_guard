# ros2_topic_guard

## 概要

ros2_topic_guard は、ROS 2 上でトピックの値を監視し、
異常な状態を検出するためのパッケージである。

本パッケージでは、例としてバッテリー残量を監視対象としている。

---

## 動作確認

- Ubuntu 22.04
- ROS 2 Humble

---

## ノード構成

本パッケージは、以下の 2 つのノードから構成される。

- **battery_publisher**
  - バッテリー残量を模擬した数値を定期的に publish するノード
- **battery_checker**
  - バッテリー残量トピックを subscribe し、値が閾値を下回った場合に警告を出力するノード
---

## トピック

| トピック名 | 型 | 説明 |
|------------|----|------|
| `/battery` | std_msgs/msg/Float32 | バッテリー残量（%）を表す数値 |

## 実行方法

---

以下のコマンドでノード群を起動できる。

```bash
ros2 launch ros2_topic_guard battery_monitor_launch.py
[INFO] [battery_publisher]: Battery: 98.3%
[INFO] [battery_checker]: Battery level OK
```
## License

SPDX-License-Identifier: GPL-3.0-only


