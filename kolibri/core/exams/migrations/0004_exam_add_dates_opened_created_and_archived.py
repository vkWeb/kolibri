# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-14 12:39
from __future__ import unicode_literals

from django.db import migrations, models

# Ensure that existing date values are initialized with a NULL value
def forward_func(apps, schema_editor):
    Exam = apps.get_model("exams", "Exam")
    Exam.objects.all().update(
        date_created=None, date_archived=None, date_activated=None
    )


class Migration(migrations.Migration):

    dependencies = [("exams", "0003_auto_20190426_1015")]

    operations = [
        migrations.AddField(
            model_name="exam",
            name="date_created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="exam",
            name="date_archived",
            field=models.DateTimeField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="exam",
            name="date_activated",
            field=models.DateTimeField(default=None, null=True, blank=True),
        ),
        # Ensure that previously created exams have no created_at by default.
        migrations.RunPython(forward_func, lambda *_: None),
    ]
