# Generated by Django 4.1.7 on 2023-03-10 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="thumbnail",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
