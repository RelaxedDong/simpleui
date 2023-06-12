# -*- coding: utf-8 -*-
import sys

from setuptools import setup

import simpleui

if sys.version_info < (3, 0):
    long_description = "\n".join([
        open('README.rst', 'r').read(),
    ])
else:
    long_description = "\n".join([
        open('README.rst', 'r', encoding='utf-8').read(),
    ])



setup(
    name='simpleui-admin',
    version=simpleui.get_version(),
    packages=['simpleui'],
    zip_safe=False,
    include_package_data=True,
    url='https://github.com/RelaxedDong/simpleui',
    license='Apache License 2.0',
    author='donghao',
    long_description=long_description,
    author_email='1417766861@qq.com',
    description='django admin theme 后台模板,后台需求定制化',
    install_requires=['django'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
