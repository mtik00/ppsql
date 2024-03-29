# ppsql

This is a simple package that is used to print the SQL-like statement crafted by Django or SQLAlchemy's ORM.

# Requirements

This package only relies on [sqlparse](https://pypi.org/project/sqlparse/) and, of course, Django or SQLAlchemy.

# Installation

You can download and install the release wheel.  You can also run this command to install the latest release:  

    pip install https://github.com/mtik00/ppsql/releases/download/v1.0.0/ppsql-1.0.0-py2.py3-none-any.whl

# Sample Usage

See the `examples` folder for Django and SQLAlchemy sample projects.

## Django
For Django queries, you can import the function one of two ways:
```python
from ppsql import ppsql
```
or the Django-specific function:
```python
from ppsql import django_ppsql
```

IPython run for the sample Django app:
```python
In [1]: from polls.models import Question, Choice

In [2]: from ppsql import ppsql

In [3]: ppsql(Question.objects.all())
SELECT "polls_question"."id",
       "polls_question"."question_text",
       "polls_question"."pub_date"
FROM "polls_question"

In [4]: ppsql(Choice.objects.filter(votes__gte=10))
SELECT "polls_choice"."id",
       "polls_choice"."question_id",
       "polls_choice"."choice_text",
       "polls_choice"."votes"
FROM "polls_choice"
WHERE "polls_choice"."votes" >= 10
```

## SQLAlchemy
For SQLAlchemy queries:
```python
from ppsql import sqlalchemy_ppsql as ppsql
```

IPython run for a sample SQLAlchemy app:
```python
In [1]: from ppsql import sqlalchemy_ppsql as ppsql, set_default_dialect

In [2]: session = create_database()

In [3]: query = session.query(User).filter(User.name == "mary")

In [4]: ppsql(query, dialect="sqlite")
SELECT users.id,
       users.name,
       users.fullname,
       users.nickname
FROM users
WHERE users.name = 'mary'

In [5]: query = session.query(User).filter(User.name.in_(("mary", "anne")))

In [6]: set_default_dialect("sqlite")

In [7]: ppsql(query)
SELECT users.id,
       users.name,
       users.fullname,
       users.nickname
FROM users
WHERE users.name IN ('mary',
                     'anne')
```
