# Generated by Django 4.0.6 on 2022-07-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_listing_category_alter_user_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image_url',
            field=models.SlugField(default=False, max_length=150),
        ),
    ]