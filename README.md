# ppsql

This is a simple package that is used to print the SQL-like statement crafted by Django's ORM.

# Requirements

This package only relies on `sqlparse` and, of course, Django.

# Sample Usage

You can use any of these methods in order to display the SQL-like query:

```python
from ppsql import ppsql

from my_project.models import User

ppsql(User.objects.all)
ppsql(User.objects.all())
ppsql(User.objects.all().query)
ppsql(str(User.objects.all().query))

print(User.objects.all, stdout=False)
```