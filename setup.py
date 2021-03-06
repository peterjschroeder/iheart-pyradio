#!/usr/bin/env python3

from distutils.core import setup

setup(
        name='iheart-pyradio', 
        version='0.1', 
        description='Fetches urls for iheartradio stations and saves them into pyradio\'s station csv.', 
        author='Peter J. Schroeder', 
        author_email='peterjschroeder@gmail.com', 
        url='https://github.com/peterjschroeder/iheart-pyradio',
        scripts=['iheart-pyradio'],
        install_requires=['iheart-mplayer @ git+https://github.com/oldlaptop/iheart-mplayer']
)

