#!/usr/bin/env python3
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution
from launch_ros.actions import Node


def generate_launch_description():
  teleop_keyboard_parameter = LaunchConfiguration(
    'teleop_keyboard_parameter',
    default=os.path.join(
      get_package_share_directory('monicar3_teleop'),
      'param/teleop_keyboard.param.yaml'
    )
  )

  return LaunchDescription([
    DeclareLaunchArgument('teleop_keyboard_parameter', default_value=teleop_keyboard_parameter
    ),

    Node(
      package='monicar3_teleop', executable='teleop_keyboard', name='teleop_keyboard_node',
      output='screen', emulate_tty=True, prefix='xterm -e',
	    parameters=[teleop_keyboard_parameter],
    ),

  ])
