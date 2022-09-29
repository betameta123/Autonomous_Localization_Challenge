import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray


class Merge_Arrays(Node):

    def __init__(self):
        super().__init__('merge_arrays_node')
        self.l1 = []
        self.l2 = []
        self.subscription1 = self.create_subscription(
            Int32MultiArray,
            '/input/array1',
            self.list1,
            10)
        self.subscription1  # prevent unused variable warning

        self.subscription2 = self.create_subscription(
            Int32MultiArray,
            '/input/array2',
            self.list2,
            10)
        self.subscription2  # prevent unused variable warning

        self.publisher_ = self.create_publisher(Int32MultiArray, '/output/array', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.array_output)

    def list1(self, msg):
        self.l1 = msg.data

    def list2(self, msg):
        self.l2 = msg.data

    def array_output(self):
        msg = Int32MultiArray()
        msg.data = (self.l1 + self.l2).sort()
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    merge_arrays = Merge_Arrays()

    rclpy.spin(merge_arrays)
    merge_arrays.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
