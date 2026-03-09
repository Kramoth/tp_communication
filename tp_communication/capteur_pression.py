import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class CapteurPression(Node):
    def __init__(self):
        super().__init__('capteur_pression')
        # Création du publisher
        self.publisher_ = self.create_publisher(
        Float32, # type de message
        'pression', # nom du topic
        10 # taille de la queue
        )
        # Timer : appelle la fonction toutes les 0.5 secondes
        self.timer = self.create_timer(0.5, self.publier_pression)
        self.get_logger().info('Capteur démarré, publication sur /pression')


    def publier_pression(self):
        msg = Float32()
        # Simule une pression entre 940hPa et 1040hPa
        msg.data = round(random.uniform(940, 1040), 2)
        self.publisher_.publish(msg)
        self.get_logger().info(f'pression publiée : {msg.data} hPa')
        
def main(args=None):
    rclpy.init(args=args)
    node =CapteurPression()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
