# Generated by Django 3.1.4 on 2020-12-24 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0012_auto_20201224_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(default=1, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]