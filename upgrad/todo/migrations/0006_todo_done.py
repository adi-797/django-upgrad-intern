# Generated by Django 2.1.7 on 2019-03-13 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_remove_todo_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.TextField(default='n'),
        ),
    ]