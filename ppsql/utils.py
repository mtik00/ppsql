#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sqlparse


def handle_sql(sql, stdout):
    formatted = sqlparse.format(sql, reindent=True, keyword_case="upper")

    if stdout:
        print(formatted)
        return

    return formatted
