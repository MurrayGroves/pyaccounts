import os
from setuptools import setup

setup(name='pyaccounts',
  version='0.2',
  author='Murrax2',
  author_email='murrax2@gmail.com',
  packages=[''],
  include_package_data=True,
  description='A Python module to make integrating accounts into your software easy.',
  install_requires=open('requirements.txt').readlines(),
  )
