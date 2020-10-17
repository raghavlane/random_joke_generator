"""This is the installation toolset for this project."""
from setuptools import setup, find_packages

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(name='random_joke_generator',
      version='0.1.0',
      author='raghav',
      description='A web server which returns a random joke with a random name.',
      long_description=long_description,
      test_suite='tests',
      packages=find_packages(exclude=('tests',)),
      entry_points={
          'console_scripts': [
              'random_joke_generator = random_joke_generator.__main__:main'
          ]
      })
