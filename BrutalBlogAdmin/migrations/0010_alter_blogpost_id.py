# Generated by Django 4.1 on 2023-01-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrutalBlogAdmin', '0009_alter_blogpost_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.CharField(default='E123C', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]