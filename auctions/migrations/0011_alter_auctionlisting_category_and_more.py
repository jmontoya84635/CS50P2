# Generated by Django 5.0.1 on 2024-01-26 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auctionlisting_users_watching'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='category',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='description',
            field=models.CharField(max_length=750),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='title',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='url',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
