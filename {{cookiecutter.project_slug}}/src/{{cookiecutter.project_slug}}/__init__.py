# -*- coding: utf-8 -*-

from {{ cookiecutter.project_slug }}.__about__ import (
    __author__, __copyright__, __email__,  __summary__, __title__,
{%- if cookiecutter.open_source_license in license_classifiers %}
    __license__,
{%- endif %}
    __uri__, __version__
)

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__copyright__",
{%- if cookiecutter.open_source_license in license_classifiers %}
    "__license__",
{%- endif %}
]
