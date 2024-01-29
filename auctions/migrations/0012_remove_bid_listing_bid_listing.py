# Generated by Django 4.2.9 on 2024-01-29 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_auctionlisting_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='listing',
        ),
        migrations.AddField(
            model_name='bid',
            name='listing',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.auctionlisting'),
            preserve_default=False,
        ),
    ]
