from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

LOCATIONS = (
    ('H', 'Home'),
    ('C', 'Cafe'),
    ('R', 'Restaurant'),
    ('F', 'Friend''s House'),
)

class Rating(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ratings_detail', kwargs={'pk' : self.id})

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(max_length=250)
    ratings = models.ManyToManyField(Rating)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'coffee_id' : self.id})

class Location(models.Model):
    date = models.DateField()
    locations = models.CharField(max_length=1, choices=LOCATIONS, default=LOCATIONS[0][0])
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_locations_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']
