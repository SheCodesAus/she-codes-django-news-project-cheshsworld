# Generated by Django 4.0.1 on 2022-02-13 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_newsstory_image_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='pub_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
