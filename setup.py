#!/usr/bin/env python

#    Copyright (C) 2014 Alexandros Avdis, Christian T. Jacobs, Gerard J. Gorman, Matthew D. Piggott.

#    This file is part of PyRDM.

#    PyRDM is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    PyRDM is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with PyRDM.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

setup(name='PyRDM',
      version='0.1a-dev',
      description='A Python program for research data management.',
      author='Alexandros Avdis, Christian T. Jacobs, Gerard J. Gorman, Matthew D. Piggott',
      url='https://bitbucket.org/ctjacobs/pyrdm',
      packages=['pyrdm'],
      package_dir = {'pyrdm': 'pyrdm'},
      scripts=["bin/pyrdm"],
      data_files=[]
     )
