# Generated by Django 4.2.5 on 2023-11-26 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0011_video_remove_project_portfolio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images_'),
        ),
    ]