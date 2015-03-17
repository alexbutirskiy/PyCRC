#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='PyCRC',
    version='1.21',
    description="Python CRC Calculations Modules",
    long_description=readme + '\n\n' + history,
    author="Cristian Năvălici",
    author_email='cristian.navalici@runbox.com',
    url='https://github.com/cristianav/PyCRC',
    packages=[
        'PyCRC',
    ],
    package_dir={'PyCRC':
                 'PyCRC'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3",
    zip_safe=False,
    keywords='PyCRC, CRC, CRC16, CRC16DNP, CRC16Kermit, CRC32',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

#  https://pypi.python.org/pypi?%3Aaction=list_classifiers
