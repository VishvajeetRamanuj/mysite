# Generated by Django 3.1.1 on 2020-09-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choice_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='answer',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default='No Answer', max_length=200),
            preserve_default=False,
        ),
    ]
