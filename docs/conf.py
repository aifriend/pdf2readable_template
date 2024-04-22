"""Sphinx configuration."""
project = "Data Science Template"
author = "Jose Lopez"
copyright = "2024, Jose Lopez"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
