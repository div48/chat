# Generated by Django 3.1.4 on 2020-12-17 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0003_auto_20201217_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pictsagram/')),
                ('image_caption', models.CharField(max_length=700)),
                ('tag_someone', models.CharField(blank=True, max_length=50)),
                ('imageuploader_profile', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image_likes', models.ManyToManyField(blank=True, default=False, related_name='likes', to='farmer.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_post', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to='farmer.profile')),
                ('commented_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.image')),
            ],
        ),
    ]