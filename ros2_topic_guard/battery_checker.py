#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Keigo Yamaguchi
# SPDX-License-Identifier: GPL-3.0-only

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class BatteryChecker(Node):
    def __init__(self):
        super().__init__('battery_checker')

        self.declare_parameter('threshold', 30.0)
        self.threshold = self.get_parameter('threshold').value

        self.subscription = self.create_subscription(
            Float32,
            'battery_level',
            self.callback,
            10
        )

    def callback(self, msg):
        if msg.data < self.threshold:
            self.get_logger().warn(f'Battery LOW: {msg.data:.1f}% (threshold {self.threshold}%)')
        else:
            self.get_logger().info(f'Battery OK: {msg.data:.1f}% (threshold {self.threshold}%)')

def main(args=None):
    rclpy.init(args=args)
    node = BatteryChecker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
