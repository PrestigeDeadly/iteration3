# Generated by Django 4.2.5 on 2023-10-03 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_delete_project_remove_student_portfolio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('contact_email', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('about', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='portfolio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio'),
            preserve_default=False,
        ),
    ]
