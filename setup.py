__author__ = 'gokhan'

from setuptools import setup

setup(
    name='postcode.io',
    packages=['lib'],
    version='0.1',
    author='Gokhan Karadas',
    author_email='gokhan.karadas1992@gmail.com',
    download_url ="https://github.com/previousdeveloper/PythonPostcodesWrapper",
    url='https://github.com/previousdeveloper/PythonPostcodesWrapper',
    license='LICENSE',
    description='Postcode & Geolocation API for UK for python',
    install_requires=['requests'],
    include_package_data=True
)

