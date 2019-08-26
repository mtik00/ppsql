#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module adds a short-cut command for printing the SQL-like text for Django
and SQLAlchemy queries.

NOTE: The default function, `ppsql`, refers to the Django function.
"""
from .django import ppsql as django_ppsql
from .sqlalchemy import ppsql as sqlalchemy_ppsql, set_default_dialect

# Set the default to use Django
ppsql = django_ppsql

__version__ = "1.0.0"
__all__ = ["sqlalchemy_ppsql", "set_default_dialect", "django_ppsql", "ppsql"]
