import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(String, 'robot_status', self.listener_callback_power, 10)
        self.subscription2 = self.create_subscription(String, 'robot_status', self.listener_callback_battery, 10)
        self.subscription3 = self.create_subscription(String, 'robot_status', self.listener_callback_pos, 10)
        self.subscription  # prevent unused variable warning
        

    def listener_callback_power(self, msg):
        if 'Robot OK' in msg.data :
            self.get_logger().info('Robot OK')

    def listener_callback_battery(self, msg):
        if 'Battery' in msg.data :
            self.get_logger().info('Battery level detected')

    def listener_callback_pos(self, msg):
        if 'Position' in msg.data :
            self.get_logger().info('Position detceted')


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
