# Generated by Django 4.1 on 2022-12-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrutalBlogAdmin', '0008_blogpost_image_url_alter_blogpost_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.CharField(default='BE388', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]
