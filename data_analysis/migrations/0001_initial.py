# Generated by Django 4.2.3 on 2023-07-19 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique_for_date='published_date')),
                ('published_date', models.DateField(default=django.utils.timezone.now)),
                ('tools_used', models.CharField(max_length=1000)),
                ('description', models.TextField(blank=True, null=True)),
                ('download_link', models.URLField(blank=True, null=True)),
                ('thumbnail', models.CharField(blank=True, max_length=500, null=True)),
                ('category', models.CharField(default='Data Science', editable=False, max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Data Analysis',
                'ordering': ('-published_date',),
            },
        ),
    ]