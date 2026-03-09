import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class Analyseur(Node):
    def __init__(self):
        super().__init__('analyseur')
        # Création du subscriber
        self.subscription_humidite = self.create_subscription(Float32,'humidite',self.humidite_callback,10)
        self.get_logger().info('Analyseur démarré, écoute sur /humidite')
        self.seuil_alerte_humidite = 80

        self.subscription = self.create_subscription(Float32,'pression',self.pression_callback,10)
        self.get_logger().info('Analyseur démarré, écoute sur /pression')
        self.seuil_alerte_pression = 950

    def humidite_callback(self, msg):
        humidite = msg.data
        if humidite > self.seuil_alerte_humidite:
            self.get_logger().warn(f'⚠️ ALERTE : {humidite}% (seuil ={self.seuil_alerte_humidite}%)')
        else:
            self.get_logger().info(f'Humidite reçue : {humidite}%')

    def pression_callback(self, msg):
        pression = msg.data
        if pression < self.seuil_alerte_pression:
            self.get_logger().warn(f'⚠️ ALERTE : {pression} hPa (seuil ={self.seuil_alerte_pression}hPa)')
        else:
            self.get_logger().info(f'Pression reçue : {pression} hPa')

def main(args=None):
    rclpy.init(args=args)
    node = Analyseur()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()