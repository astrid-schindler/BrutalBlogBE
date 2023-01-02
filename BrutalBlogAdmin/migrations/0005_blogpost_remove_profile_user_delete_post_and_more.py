# Generated by Django 4.1 on 2022-12-30 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrutalBlogAdmin', '0004_rename_category_tag_rename_categories_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('title', models.CharField(max_length=255, unique=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('published', models.BooleanField(default=False)),
                ('author', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]