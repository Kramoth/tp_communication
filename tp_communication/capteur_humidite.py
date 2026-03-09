import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class CapteurHumidite(Node):
    def __init__(self):
        super().__init__('capteur_humidite')
        # Création du publisher
        self.publisher_ = self.create_publisher(
        Float32, # type de message
        'humidite', # nom du topic
        10 # taille de la queue
        )
        # Timer : appelle la fonction toutes les 0.5 secondes
        self.timer = self.create_timer(0.5, self.publier_humidite)
        self.get_logger().info('Capteur démarré, publication sur /humidite')


    def publier_humidite(self):
        msg = Float32()
        # Simule une humidite entre 20% et 90%
        msg.data = round(random.uniform(40.0, 95.0), 2)
        self.publisher_.publish(msg)
        self.get_logger().info(f'humidite publiée : {msg.data}%')
        
def main(args=None):
    rclpy.init(args=args)
    node =CapteurHumidite()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
