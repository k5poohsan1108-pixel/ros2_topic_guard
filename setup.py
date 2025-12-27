from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ros2_topic_guard'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yamaguchi',
    maintainer_email='k5poohsan1108@gmail.com',
    description='Detects abnormal values from a ROS 2 topic',
    license='GPL-3.0-only',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'battery_publisher = ros2_topic_guard.battery_publisher:main',
            'battery_checker = ros2_topic_guard.battery_checker:main',
        ],
    },
)

