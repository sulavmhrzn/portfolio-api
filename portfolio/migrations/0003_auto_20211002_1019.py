# Generated by Django 3.2.7 on 2021-10-02 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_aboutme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutme',
            name='skill',
        ),
        migrations.AddField(
            model_name='aboutme',
            name='skill',
            field=models.ManyToManyField(to='portfolio.Skill'),
        ),
    ]
