from setuptools import find_packages, setup

package_name = 'tp_communication'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='khadim',
    maintainer_email='khadim@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'capteur_temperature = tp_communication.capteur_temperature:main',
            'capteur_humidite = tp_communication.capteur_humidite:main',
            'capteur_pression = tp_communication.capteur_pression:main',
            'afficheur_temperature = tp_communication.afficheur_temperature:main',
            'analyseur = tp_communication.analyseur:main'
            
        ],
    },
)
