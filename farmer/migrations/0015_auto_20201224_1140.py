# Generated by Django 3.1.4 on 2020-12-24 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0014_auto_20201224_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]