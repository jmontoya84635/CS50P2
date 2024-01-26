from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, AuctionListing
from django.contrib import messages


def index(request):
    return render(request, "auctions/index.html", {
        "AuctionListings": AuctionListing.objects.all()
    })


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.warning(request, "Invalid username and/or password.")
            return render(request, "auctions/login.html")
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            messages.error(request, "Passwords must match.", extra_tags="danger")
            return render(request, "auctions/register.html")

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            messages.error(request, "Username already taken.", extra_tags="danger")
            return render(request, "auctions/register.html")
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def createListing(request, username):
    if not request.user.is_authenticated:
        messages.error(request, "You are not signed in!")
        return HttpResponseRedirect(reverse("login"))
    if request.user.username != username:
        messages.error(request, "You do not have access to this page!", extra_tags="danger")
        return HttpResponseRedirect(reverse("index"))

    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        startingBid = int(request.POST["startingBid"])
        image = request.POST["image"]

        listing = AuctionListing(
            title=title,
            description=description,
            startingBid=startingBid,
            url=image,
            creator=request.user,
        )
        listing.save()
        return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/createListing.html")


def watchlist(request, username):
    if not request.user.is_authenticated:
        messages.error(request, "You need to log in to create a listing", extra_tags="danger")
        return HttpResponseRedirect(reverse("login"))
    if request.user.username != username:
        return HttpResponseRedirect(reverse("index"), {
            "alert": True,
        })
    return render(request, "auctions/watchlist.html", {
        "listings": request.user.watchlistItems.all(),
    })


def categoryView(request):
    return render(request, "auctions/category.html")


def listingView(request, listingId):
    isAlreadyIn = False
    watchlist_list = request.user.watchlistItems.all()
    currListing = AuctionListing.objects.get(pk=listingId)
    if currListing in watchlist_list:
        isAlreadyIn = True
    for item in watchlist_list:
        print(item)
    if request.method == "POST":
        if request.user.is_authenticated:
            listing = AuctionListing.objects.get(pk=listingId)
            listing.users_watching.add(request.user)
            listing.save()
            messages.success(request, "Saved item to your watchlist")
            return HttpResponseRedirect(reverse("listingView", kwargs={
                'listingId': listingId,
            }))

    listing = AuctionListing.objects.get(pk=listingId)

    return render(request, "auctions/viewpage.html", {
        "listing": listing,
        "isAlreadyIn": isAlreadyIn,
    })
