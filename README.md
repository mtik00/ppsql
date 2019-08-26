# ppsql

This is a simple package that is used to print the SQL-like statement crafted by Django or SQLAlchemy's ORM.

# Requirements

This package only relies on `sqlparse` and, of course, Django or SQLAlchemy.

# Sample Usage

## Django
```python
In [1]: from polls.models import Question, Choice

In [2]: from ppsql import django_ppsql as ppsql

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
```python
In [1]: from ppsql import sqlalchemy_ppsql as ppsql

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

In [6]: ppsql(query, dialect="sqlite")
SELECT users.id,
       users.name,
       users.fullname,
       users.nickname
FROM users
WHERE users.name IN ('mary',
                     'anne')
```
