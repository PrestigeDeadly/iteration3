# Generated by Django 4.2.5 on 2023-10-19 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0009_alter_portfolio_managers_alter_project_managers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectsInPortfolio',
        ),
    ]
