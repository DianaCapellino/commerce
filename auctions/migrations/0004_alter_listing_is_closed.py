# Generated by Django 4.0.6 on 2022-07-27 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_bid_comment_watchlist_alter_user_birthday_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='is_closed',
            field=models.BooleanField(default=None),
        ),
    ]
