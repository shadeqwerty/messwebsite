from django.db import models
from django.contrib.auth.models import User

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
        return f'Review by {self.user.username} on {self.food_item.name}'