# Generated by Django 3.2.7 on 2021-10-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='certificate',
            field=models.ManyToManyField(blank=True, to='portfolio.Certificate'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='education',
            field=models.ManyToManyField(blank=True, to='portfolio.Education'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='profile',
            field=models.ManyToManyField(blank=True, to='portfolio.Profile'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='project',
            field=models.ManyToManyField(blank=True, to='portfolio.Project'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='skill',
            field=models.ManyToManyField(blank=True, to='portfolio.Skill'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='work',
            field=models.ManyToManyField(blank=True, to='portfolio.Work'),
        ),
    ]
