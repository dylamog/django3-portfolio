# Generated by Django 5.0.2 on 2024-02-25 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogpost",
            name="image",
        ),
        migrations.RemoveField(
            model_name="blogpost",
            name="url",
        ),
        migrations.AddField(
            model_name="blogpost",
            name="date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 2, 25, 9, 26, 48, 920857, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]
