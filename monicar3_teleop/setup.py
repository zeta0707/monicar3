import os
from glob import glob
from setuptools import find_packages
from setuptools import setup

package_name = 'monicar3_teleop'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=[]),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'param'), glob('param/*.yaml')),
    ],
    install_requires=[
        'setuptools',
    ],
    zip_safe=True,
    author='ChangWhan Lee',
    author_email='zeta0707@gmail.com',
    maintainer='ChangWhan Lee',
    maintainer_email='zeta0707@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'Teleoperation node using keyboard or joystick for the Monicar3'
    ),
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop_keyboard = monicar3_teleop.teleop_keyboard:main',
            'teleop_joy = monicar3_teleop.teleop_joy:main'
        ],
    },
)
