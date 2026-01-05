#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Keigo Yamaguchi
# SPDX-License-Identifier: GPL-3.0-only

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Int8

class BatteryChecker(Node):

    def __init__(self):
        super().__init__('battery_checker')

        self.low_threshold = 30.0
        self.critical_threshold = 10.0

        self.sub = self.create_subscription(
            Float32,
            'battery_level',
            self.callback,
            10
        )

        self.state_pub = self.create_publisher(
            Int8,
            'battery_state',
            10
        )

    def callback(self, msg):
        level = msg.data
        state = Int8()

        self.get_logger().info(f"callback called: {msg.data}")

        if level < self.critical_threshold:
            state.data = 2
            self.get_logger().error('Battery CRITICAL')
        elif level < self.low_threshold:
            state.data = 1
            self.get_logger().warning('Battery LOW')
        else:
            state.data = 0
            self.get_logger().info('Battery OK')

        self.state_pub.publish(state)


def main():
    rclpy.init()
    node = BatteryChecker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
