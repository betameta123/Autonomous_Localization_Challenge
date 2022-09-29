from setuptools import setup

package_name = 'merge_arrays_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kyle',
    maintainer_email='kkhuang@wisc.edu',
    description='Merge two sorted arrays into one larger sorted array',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = merge_arrays_node.challenge:main'
        ],
    },
)
