# Generated by Django 3.2.7 on 2021-10-02 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('label', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='profile')),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('phone', models.CharField(blank=True, default='', max_length=10)),
                ('summary', models.TextField()),
                ('blog', models.URLField(blank=True, default='')),
                ('Education', models.ManyToManyField(to='portfolio.Education')),
                ('certificate', models.ManyToManyField(to='portfolio.Certificate')),
                ('profile', models.ManyToManyField(to='portfolio.Profile')),
                ('project', models.ManyToManyField(to='portfolio.Project')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.skill')),
                ('work', models.ManyToManyField(to='portfolio.Work')),
            ],
        ),
    ]
