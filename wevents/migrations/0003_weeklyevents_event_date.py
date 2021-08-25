# Generated by Django 3.0.1 on 2021-08-22 14:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wevents', '0002_remove_weeklyevents_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklyevents',
            name='event_date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2021, 8, 22, 14, 57, 20, 466424, tzinfo=utc)),
            preserve_default=False,
        ),
    ]