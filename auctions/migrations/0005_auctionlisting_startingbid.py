# Generated by Django 5.0.1 on 2024-01-22 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_auctionlisting_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='startingBid',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
