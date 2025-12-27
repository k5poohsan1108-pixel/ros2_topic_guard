import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class BatteryPublisher(Node):
    def __init__(self):
        super().__init__('battery_publisher')
        self.publisher_ = self.create_publisher(Float32, 'battery_level', 10)
        self.timer = self.create_timer(1.0, self.publish_battery)
        self.battery_level = 100.0

    def publish_battery(self):
        self.battery_level -= random.uniform(0, 5)
        if self.battery_level < 0:
            self.battery_level = 100.0
        msg = Float32()
        msg.data = self.battery_level
        self.publisher_.publish(msg)
        self.get_logger().info(f'Battery: {msg.data:.1f}%')

def main(args=None):
    rclpy.init(args=args)
    node = BatteryPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
