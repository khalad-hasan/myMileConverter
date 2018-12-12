from setuptools import setup, find_packages

setup(
    name='my-mile-converter',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An test python package to convert to miles',
    author='MK Hasan',
    author_email='khalad.hasan@gmail.com'
)