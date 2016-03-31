#!/usr/bin/env python

import setuptools
try:
  import multyprocessing 
except ImportError:
  pass
setuptools.setup( setup_requires=['pbr'],pbr=True)

