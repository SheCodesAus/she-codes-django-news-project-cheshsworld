# Generated by Django 4.0.1 on 2022-02-12 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_newsstory_image_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image_upload',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
