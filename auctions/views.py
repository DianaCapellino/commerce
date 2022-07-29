from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from .models import User, Listing, Bid, Comment, ListingForm, Watchlist


# Default page with the listings
def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        birthday = request.POST["birthday"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create_listing(request):
    
    # If method is POST it will create the new listing with the user id
    if request.method == "POST":

        form = ListingForm(request.POST)

        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.user_id = request.POST["user_id"]
            new_listing.username = User.objects.get(pk=new_listing.user_id).username
            new_listing.current_price = new_listing.starting_bid
            new_listing.save()
            form.save_m2m()

            # After saving the listing it redirects to the main page
            return HttpResponseRedirect(reverse("index"))
        
        # If there are any errors in the form, it will display the form again
        else:
            return render(request, "auctions/new_listing.html", {
                "form": form
            })
    
    # If method is GET it displays the form to add new listing
    else:
        return render(request, "auctions/new_listing.html", {
            "form": ListingForm()
        })

# This is the function to display particular listing with id
def display_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)

    # Get the quantity of bids for that listing to display later
    bid_list = listing.bid_listings.all()
    bid_lenght = len(bid_list)

    # Get the info if the user has or not the listing in the watchlist
    user_all_watchlist = Watchlist.objects.filter(user_id=request.user.id)
    user_listing_watchlist = user_all_watchlist.filter(listing_id=listing_id)

    if not user_listing_watchlist:
        is_watching = False
    else:
        is_watching = True

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "bid_lenght": bid_lenght,
        "is_watching": is_watching
    })

# This will create new bid when pressing BID in the listing item
@login_required
def new_bid(request, listing_id):

    # Get the information needed from the form
    bid = float(request.POST["bid"])
    user_id = request.POST["user_id"]

    # Get the objects from the id got in the form
    listing = Listing.objects.get(pk=listing_id)
    user = User.objects.get(pk=user_id)

    # Get the list of bids and the lenght
    bid_list = listing.bid_listings.all()
    bid_lenght = len(bid_list)
    
    # Check if the bid is larger than the current price
    if (bid_lenght == 0 and bid >= listing.starting_bid) or (bid_lenght > 0 and bid > listing.current_price):

        # Create a new bid
        new_bid = Bid(user_id=user, listing_id=listing, amount=bid)
        new_bid.save()

        # Update current price in the listing
        listing.current_price = bid
        listing.save()

        # Redirect to Listing to see updated rate
        return HttpResponseRedirect(reverse("listing", args=(listing_id)))
    else:
        return HttpResponseRedirect(reverse("error"))

# It is called when pressing "Add to watchlist" in listing
@login_required
def watch(request, listing_id):
    if request.method == "POST":
        user_id = request.user.id
        listing = Listing.objects.get(pk=listing_id)
        user = User.objects.get(pk=user_id)
        
        user_all_watchlist = Watchlist.objects.filter(user_id=request.user.id)
        user_listing_watchlist = user_all_watchlist.filter(listing_id=listing_id)

        if not user_listing_watchlist:
            new_watcher = Watchlist(user_id=user_id, listing_id=listing_id)
            new_watcher.save()
        else:          
            old_watcher = user_listing_watchlist
            old_watcher.delete()

        return HttpResponseRedirect(reverse("listing", args=(listing_id)))

@login_required
def watchlist(request):

    user_all_watchlist = Watchlist.objects.filter(user_id=request.user.id)

    user_watchlist = []
    for listing in user_all_watchlist:
        user_watchlist.append(Listing.objects.get(pk=listing.listing_id))


    return render(request, "auctions/watchlist.html", {
        "watchlist": user_watchlist
    })
    
def error(request):
    return render(request, "auctions/error.html", {
        "message": "Your bid should be at least larger than the current price or equal to the starting bid."
    })