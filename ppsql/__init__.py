#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module adds a short-cut command for printing the SQL-like text for Django
and SQLAlchemy queries.

NOTE: The default function, `ppsql`, refers to the Django function.
"""

from __future__ import print_function
import sqlparse

__version__ = "1.0.0"


DEFAULT_DIALECT = None


def django_ppsql(sql, stdout=True):
    """
    Print or return the converted query.

    The input can be a QuerySet (e.g. `MyModel.objects.all()`), a Query (e.g.
    `MyModel.objects.all().query`), a callable (e.g. `MyModel.objects.all`),
    or a string (e.g. `str(MyModel.objects.all().query)`).

    :param * sql: See above
    :param bool stdout: This function will print to STDOUT when True.  NOTE:
        In order to keep debugging less noisy, `stdout=TRUE` will **not** return
        the formatted string.
    :returns: the formatted string
    """
    from django.db.models.sql.query import Query
    from django.db.models.query import QuerySet

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


def sqlalchemy_ppsql(sql, stdout=True, dialect=None):
    """
    Print or return the converted query.

    The input can be a Query (e.g. `session.query(MyModel)`) or a string (e.g.
    `str(session.query(MyModel))`).

    # Dialects

    sqlalchemy uses dialects to communicate with various backends.  You may
    want to use a dialect when compiling the SQL string.

    See here for more information:

        https://docs.sqlalchemy.org/en/13/dialects/

    As a convenience, the following strings are supported.

        "postgresql", "sqlite", "mysql"

    You may also pass in the dialect directly:

        from sqlalchemy.dialects import firebird
        print(sqlalchemy_ppsql(q, dialect=firebird.dialect()))

    You may also call `set_default_dialect()` so you don't have too keep passing
    in this parameter.

    :param * sql: See above
    :param bool stdout: This function will print to STDOUT when True.  NOTE:
        In order to keep debugging less noisy, `stdout=TRUE` will **not** return
        the formatted string.
    :param str dialect: The dialect to use, if needed.  See note.
    :returns: the formatted string
    """
    from sqlalchemy.orm.query import Query
    from sqlalchemy.dialects import postgresql, sqlite as sqlite_dialect, mysql

    # Only use the default dialect if it has been set.  Otherwise allow `None`
    # to fall through.
    if (dialect is None) and (DEFAULT_DIALECT is not None):
        dialect = DEFAULT_DIALECT

    dialect_map = {
        "postgresql": postgresql.dialect(),
        "sqlite": sqlite_dialect.dialect(),
        "mysql": mysql.dialect(),
    }

    if dialect:
        try:
            dialect = dialect_map[dialect]
        except KeyError:
            dialect = dialect

    if callable(sql):
        sql = str(sql)

    if isinstance(sql, Query):
        # Attempt to replace '?' with the actual values
        try:
            sql = str(
                sql.statement.compile(
                    dialect=dialect, compile_kwargs={"literal_binds": True}
                )
            )
        except Exception:
            sql = str(sql.statement.compile(dialect=dialect))

    formatted = sqlparse.format(sql, reindent=True, keyword_case="upper")

    if stdout:
        print(formatted)
        return

    return formatted


def set_default_dialect(dialect):
    """
    Forces all subsequent `sqlalchemy_ppsql()` calls to use the provided
    dialect.

    You must use `set_default_dialect(None)` to revert this behavior.
    """
    global DEFAULT_DIALECT
    DEFAULT_DIALECT = dialect


# Set the default to use Django
ppsql = django_ppsql
