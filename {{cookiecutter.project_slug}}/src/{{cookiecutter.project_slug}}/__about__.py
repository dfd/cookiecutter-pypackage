# -*- coding: utf-8 -*-

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__copyright__", 
{%- if cookiecutter.open_source_license in license_classifiers %}
"__license__",
{%- endif %}
]


__title__ = "{{ cookiecutter.project_slug }}"
__summary__ = "{{ cookiecutter.project_short_description }}"
__uri__ = "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}"

__version__ = "{{ cookiecutter.version }}"

__author__ = "{{ cookiecutter.full_name.replace('\"', '\\\"') }}"
__email__ = "{{ cookiecutter.email }}"

__copyright__ = "Copyright 2017 {0}".format(__author__)

{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
