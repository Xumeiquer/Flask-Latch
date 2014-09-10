"""
Flask-Latch
-------------

Latch extension for Flask
"""
from __future__ import with_statement
from setuptools import setup

setup(
    name='Flask-Latch',
    version='0.0.1',
    url='https://github.com/Xumeiquer/Flask-Latch',
    license='MIT',
    author='Jaume Martin',
    author_email='jaumartin@gmail.com',
    description='Latch extension for Flask',
    long_description=__doc__,
    packages=['flask_Latch'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.8'
    ],
    classifiers=[
        'Development Status :: Development',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)