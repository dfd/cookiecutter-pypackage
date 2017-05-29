#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os, sys

base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, "src")

sys.path.insert(0, src_dir)

about = {}
with open(os.path.join(src_dir, "{{ cookiecutter.project_slug }}", "__about__.py")) as f:
    exec(f.read(), about)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    {%- if cookiecutter.command_line_interface|lower == 'click' %}
    'Click>=6.0',
    {%- endif %}
    # TODO: put package requirements here
]

test_requirements = [
    'pytest'
]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__summary__'],
    long_description=readme + '\n\n' + history,
    author=about['__author__'],
    author_email=about['__email__'],
    url=about['__uri__'],
{%- if cookiecutter.open_source_license in license_classifiers %}
    license=about['__license__'],
{%- endif %}
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main'
        ]
    },
    {%- endif %}
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
