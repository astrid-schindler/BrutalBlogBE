# Generated by Django 4.1 on 2022-12-28 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BrutalBlogAdmin', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tags',
            new_name='categories',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subtitle',
        ),
    ]
