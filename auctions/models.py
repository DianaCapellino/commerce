from django.contrib.auth.models import AbstractUser
from django.db import models
import django.utils.timezone
from django.forms import ModelForm

CATEGORIES = [
    ("Toys", "Toys"),
    ("Fashion", "Fashion"),
    ("Electronics", "Electronics"),
    ("Home", "Home"),
    ("Pets", "Pets"),
    ("Others", "Others")
]

class User(AbstractUser):

    def __str__(self):
        return f"{self.username}"


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    starting_bid = models.FloatField()
    current_price = models.FloatField(null=True)
    image_url = models.CharField(max_length=512, blank=True)
    category = models.CharField(max_length=64, choices=CATEGORIES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner_user")
    username = models.CharField(max_length=64)
    watching = models.ManyToManyField(User, blank=True, related_name="watch_users")
    starting_date = models.DateTimeField(default=django.utils.timezone.now, verbose_name='starting date')
    closing_date = models.DateTimeField(default=django.utils.timezone.now, verbose_name='closing date')
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            'title',
            'description',
            'starting_bid',
            'image_url',
            'category'
        ]


class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid_users")
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid_listings")
    amount = models.FloatField()
    date = models.DateTimeField(auto_now=True, verbose_name='bid_date')

    def __str__(self):
        return f"USD {self.amount}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_users")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comment_listings")
    comment = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.comment} (by: {self.user})"