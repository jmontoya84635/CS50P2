# Generated by Django 5.0.1 on 2024-01-24 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auctionlisting_startingbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.RemoveField(
            model_name='bid',
            name='bidder',
        ),
        migrations.AlterField(
            model_name='bid',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.ManyToManyField(to='auctions.auctionlisting'),
        ),
    ]
