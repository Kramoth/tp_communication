import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random
class CapteurTemperature(Node):
    def __init__(self):
        super().__init__('capteur_temperature')
        # Création du publisher
        self.publisher_ = self.create_publisher(
        Float32, # type de message
        'temperature', # nom du topic
        10 # taille de la queue
        )
        # Timer : appelle la fonction toutes les 0.5 secondes
        self.timer = self.create_timer(0.5, self.publier_temperature)
        self.get_logger().info('Capteur démarré, publication sur /temperature')


    def publier_temperature(self):
        msg = Float32()
        # Simule une température entre 18.0 et 35.0 °C
        msg.data = round(random.uniform(18.0, 35.0), 2)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Température publiée : {msg.data} °C')
        
def main(args=None):
    rclpy.init(args=args)
    node = CapteurTemperature()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
