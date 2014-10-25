#!/usr/bin/env python
#-*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(
        console=[
            {
                'script': 'app.py',
                'icon_resources':[ (0,'./img/icon.ico') ]
            }
        ],
        options={
                'py2exe': { 
                    'compressed': 1,
                    'optimize': 2,
                    'dist_dir': './dist',
                    'bundle_files': 1,
                    'includes': ['twisted', 'zope.interface']
                    }
        },
        zipfile = None,
    )
