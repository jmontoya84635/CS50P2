from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create/<str:username>", views.createListing, name="create"),
    path("watch/<str:username>", views.watchlist, name="watchlist"),
    path("category", views.categoryView, name="category"),
    path("view/<str:listingId>", views.listingView, name="listingView"),
]
