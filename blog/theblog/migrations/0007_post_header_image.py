# Generated by Django 3.1.5 on 2021-02-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
