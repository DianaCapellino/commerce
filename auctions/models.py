from django.contrib.auth.models import AbstractUser
from django.db import models
import django.utils.timezone
from django.forms import ModelForm

CATEGORIES = [
    ("1", "Toys"),
    ("2", "Fashion"),
    ("3", "Electronics"),
    ("4", "Home"),
    ("5", "Pets"),
    ("6", "Others")
]

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class User(AbstractUser):
    birthday = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    starting_bid = models.FloatField()
    image_url = models.SlugField(max_length=150, default=None)
    category = models.CharField(max_length=64, choices=CATEGORIES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner_user")
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
    pass

class Comment(models.Model):
    pass

class Watchlist(models.Model):
    pass