#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module add a short-cut command for printing the SQL-like text for Django
queries.
"""

from __future__ import print_function
import sqlparse
from django.db.models.sql.query import Query
from django.db.models.query import QuerySet

__version__ = "0.1.0"


def ppsql(sql, stdout=True):
    """
    Prints the converted query.

    The input can be a QuerySet (e.g. `MyModel.objects.all()`), a Query (e.g.
    `MyModel.objects.all().query`), a callable (e.g. `MyModel.objects.all`),
    or a string (e.g. `str(MyModel.objects.all().query)`).

    :param * sql: See above
    :param bool stdout: This function will print to STDOUT when True.  NOTE:
        In order to keep debugging less noisy, `stdout=TRUE` will **not** return
        the formatted string.
    :returns: the formatted string

    NOTE: This function does not return the formatting string; the formatted
    string is sent to `STDOUT`.
    """
    if callable(sql):
        # Make the query.  This will return a QuerySet
        sql = sql()

    if isinstance(sql, Query):
        sql = str(sql)
    elif isinstance(sql, QuerySet):
        sql = str(sql.query)

    formatted = sqlparse.format(sql, reindent=True, keyword_case="upper")

    if stdout:
        print(formatted)
        return

    return formatted