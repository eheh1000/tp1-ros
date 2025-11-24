import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(String, 'sensor/lidar', self.listener_callback_lidar, 10)
        self.subscription2 = self.create_subscription(String, 'sensor/camera', self.listener_callback_camera, 10)
        self.subscription3 = self.create_subscription(String, 'sensor/imu', self.listener_callback_imu, 10)
        self.subscription  # prevent unused variable warning
        

    def listener_callback_lidar(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

    def listener_callback_camera(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

    def listener_callback_imu(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


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
