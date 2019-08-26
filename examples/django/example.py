# -*- coding: utf-8 -*-
# Django setup #######################################################
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django  # noqa: E402

django.setup()
#######################################################################


if __name__ == "__main__":
    from polls.models import Question, Choice  # noqa: E402
    from ppsql import ppsql  # noqa: E402

    ppsql(Question.objects.all())
    ppsql(Choice.objects.filter(votes__gte=10))
