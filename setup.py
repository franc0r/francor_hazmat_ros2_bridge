import os
from glob import glob
from setuptools import setup

package_name = 'francor_hazmat_ros2_bridge'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.py')),
        (os.path.join('share', package_name, 'docker'), glob('docker/*.yaml')),
        (os.path.join('share', package_name, 'docker', 'ohm_rrl_perception'), glob('docker/ohm_rrl_perception/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Martin Bauernschmitt',
    maintainer_email='martin.bauernschmitt@francor.de',
    description='ROS2 bridge for HAZMAT detection from ohm_rrl_perception',
    license='BSD 3-clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            ''
        ],
    },
)
