from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listing/<str:listing_id>", views.display_listing, name="listing"),
    path("listing/<str:listing_id>/new_bid", views.new_bid, name="new_bid"),
    path("listing/<str:listing_id>/watch", views.watch, name="watch"),
    path('watchlist', views.watchlist, name="watchlist"),
    path("error", views.error, name="error")
]
