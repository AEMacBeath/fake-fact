# Generated by Django 3.2.14 on 2022-07-23 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]