from django.db import models
from django.contrib.auth.models import User
class MenuItem(models.Model):
    DAYS_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    SESSION_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Snacks', 'Snacks'),
        ('Dinner', 'Dinner'),
    ]

    WEEK_TYPE_CHOICES = [
        ('Odd', 'Odd'),
        ('Even', 'Even'),
    ]

    day = models.CharField(max_length=9, choices=DAYS_CHOICES)
    session = models.CharField(max_length=9, choices=SESSION_CHOICES)
    week_type = models.CharField(max_length=4, choices=WEEK_TYPE_CHOICES)
    food_item = models.CharField(max_length=255)
    
class FoodItem(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
RATING_CHOICES = [
    (-1, 'Removal Request'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES,  default=1)
    comments = models.TextField(default='')
    def __str__(self):
        return f'Review  by {self.user.username} on {self.food_item.name}'