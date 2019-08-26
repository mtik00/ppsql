# -*- coding: utf-8 -*-
from __future__ import print_function
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django  # noqa: E402

django.setup()


from polls.models import Question, Choice  # noqa: E402
from ppsql import django_ppsql as ppsql  # noqa: E402

ppsql(Question.objects.all())
ppsql(Choice.objects.filter(votes__gte=10))
