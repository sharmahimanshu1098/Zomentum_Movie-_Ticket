# Generated by Django 3.0 on 2020-02-11 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movies_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='up',
            field=models.BooleanField(default=False),
        ),
    ]
