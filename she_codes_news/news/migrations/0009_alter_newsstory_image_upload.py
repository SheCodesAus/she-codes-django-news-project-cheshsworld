# Generated by Django 4.0.1 on 2022-02-17 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_newsstory_pub_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image_upload',
            field=models.URLField(default='https://picsum.photos/600'),
        ),
    ]
