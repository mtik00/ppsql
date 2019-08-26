# ppsql

This is a simple package that is used to print the SQL-like statement crafted by Django or SQLAlchemy's ORM.

# Requirements

This package only relies on `sqlparse` and, of course, Django or SQLAlchemy.

# Sample Usage

## Django

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
