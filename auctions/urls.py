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
    path("listing/<str:listing_id>/close", views.close, name="close"),
    path("listing/<str:listing_id>/add_comment", views.add_comment, name="add_comment"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("error", views.error, name="error")
]
