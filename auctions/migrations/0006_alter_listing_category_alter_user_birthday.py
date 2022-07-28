# Generated by Django 4.0.6 on 2022-07-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_rename_user_id_listing_user_alter_listing_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('1', 'Toys'), ('2', 'Fashion'), ('3', 'Electronics'), ('4', 'Home'), ('5', 'Pets'), ('6', 'Others')], max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]