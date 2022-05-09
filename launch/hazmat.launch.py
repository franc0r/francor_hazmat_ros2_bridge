from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions.execute_process import ExecuteProcess
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    docker_compose_path = str(get_package_share_directory('francor_hazmat_ros2_bridge') + "/docker")
    return LaunchDescription([
        ExecuteProcess(
            cmd = ['docker-compose', 'up'],
            cwd = docker_compose_path,
            name='HAZMAT ROS1 Bridge Docker',
            output='both',
        )
    ])