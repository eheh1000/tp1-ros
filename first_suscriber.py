import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription1 = self.create_subscription(
            String,
            'topic',
            self.listener_callback1,
            10)
        self.subscription1 # prevent unused variable warning

        self.subscription2 = self.create_subscription(
            String,
            'topic',
            self.listener_callback2,
            10)
        self.subscription2 # prevent unused variable warning

        self.subscription3 = self.create_subscription(
            String,
            'topic',
            self.listener_callback3,
            10)
        self.subscription3 # prevent unused variable warning

    #On récupère le message publié on vérifie que Robot soit OK 
    def listener_callback1(self, msg):
        if 'Robot OK' in msg.data:
            self.get_logger().info('Robot status : OK')
        else :
            self.publisher_ = self.create_publisher(String, 'topic', 10)
            self.get_logger().info('Robot status : OK n est pas recu')



    #Ensuite on extrait les informations de batterie et position et on les affiche
    def listener_callback2(self, msg):
        if 'Robot OK' in msg.data:
            battery_info = msg.data.split('Battery: ')[1].split('%,')[0]
            self.get_logger().info('Battery Level: %s%%' % battery_info)

    def listener_callback3(self, msg):
        if 'Robot OK' in msg.data:
            position_info = msg.data.split('Position: (')[1].split(')')[0]
            self.get_logger().info('Position: (%s)' % position_info)
    

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
