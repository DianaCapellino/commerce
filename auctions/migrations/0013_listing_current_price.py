# Generated by Django 4.0.6 on 2022-07-28 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_listing_username_alter_listing_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='current_price',
            field=models.FloatField(null=True),
        ),
    ]
