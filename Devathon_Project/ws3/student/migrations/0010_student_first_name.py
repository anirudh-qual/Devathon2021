# Generated by Django 3.2.7 on 2021-09-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20210918_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
