#!/usr/bin/env python

from setuptools import setup

setup(name = 'jkstyles',
      version = '4',
      description = 'Some pygment styles for LaTeX primarily.',
      author = 'Jonas Kalderstam',
      author_email = 'jonas@kalderstam.se',
      url = 'https://github.com/spacecowboy/',
      packages = ['jkstyles'],
      package_dir = {'jkstyles': 'jkstyles'},
      install_requires = ['pygments'],
      entry_points = '''
        [pygments.styles]
        jkdefault = jkstyles:JKDefaultStyle
        '''
    )
