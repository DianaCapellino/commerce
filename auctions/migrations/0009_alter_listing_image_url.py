# Generated by Django 4.0.6 on 2022-07-28 15:13

import auctions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_listing_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image_url',
            field=models.ImageField(upload_to=auctions.models.user_directory_path),
        ),
    ]
