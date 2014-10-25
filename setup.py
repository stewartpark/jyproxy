#!/usr/bin/env python
#-*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(
        console=['app.py'],
        options={
                'py2exe': { 
                    'compressed': 1,
                    'optimize': 2,
                    'dist_dir': './dist',
                    'bundle_files': 1
                    }
        },
        zipfile = None,
        icon_resource='./img/icon.ico'
    )
