from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser, models.Model):
    pass


class AuctionListing(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=500)
    url = models.CharField(blank=True, max_length=250)
    category = models.CharField(blank=True, max_length=15)
    startingBid = models.IntegerField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings_By_user")

    def __str__(self):
        return f'listing for:{self.title}'


class Bid(models.Model):
    amount = models.IntegerField()
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="bids")
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f'bid for {self.amount}, on {self.listing}'


class Comment(models.Model):
    text = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Comment")
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="Comments")

    def __str__(self):
        return f'{self.user} commented {self.text} on {self.listing}'
