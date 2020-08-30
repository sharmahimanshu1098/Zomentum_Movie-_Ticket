# Generated by Django 3.0 on 2020-02-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('duration', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
                ('cast', models.TextField(max_length=100)),
                ('trailer', models.CharField(max_length=100)),
            ],
        ),
    ]
