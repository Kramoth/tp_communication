import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class AfficheurTemperature(Node):
    def __init__(self):
        super().__init__('afficheur_temperature')
        # Création du subscriber
        self.subscription = self.create_subscription(
        Float32, # type de message
        'temperature', # nom du topic
        self.callback, # fonction appelée à chaque message
        10 # taille de la queue
        )
        self.get_logger().info('Afficheur démarré, écoute sur /temperature')
        self.seuil_alerte = 30.0

    def callback(self, msg):
        temp = msg.data
        if temp > self.seuil_alerte:
            self.get_logger().warn(f'⚠️ ALERTE : {temp} °C (seuil ={self.seuil_alerte} °C)')
        else:
            self.get_logger().info(f'Température reçue : {temp} °C')

def main(args=None):
    rclpy.init(args=args)
    node = AfficheurTemperature()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()