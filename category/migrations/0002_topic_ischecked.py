# Generated by Django 3.0.1 on 2019-12-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='ischecked',
            field=models.BooleanField(default=False),
        ),
    ]
