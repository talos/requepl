#!/usr/bin/env python

try:
    # Install prereqs here and now if we can.
    from setuptools import setup
    kw = {
        'install_requires': ['requests>=0.8.0']
        }
except ImportError:
    from distutils.core import setup
    print 'No setuptools.  You may have to manually install dependencies.'
    kw = {}

setup(name='requepl',
      license='GPLv3',
      version='0.0.12',
      description='HTTP REPL with multiple sessions.',
      author='John Krauss',
      author_email='irving.krauss@gmail.com',
      url='http://github.com/talos/requepl',
      scripts=['requepl'],
      **kw
      )
