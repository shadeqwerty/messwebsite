from django import forms
from .models import Review, MenuItem

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comments',]

class FilterForm(forms.Form):
    SESSION_CHOICES = [
        ('All', 'All'),
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Snacks', 'Snacks'),
        ('Dinner', 'Dinner'),
    ]
    WEEK_TYPE_CHOICES = [
        ('', 'Select...'),
        ('Odd', 'Odd'),
        ('Even', 'Even'),
    ]
    DAY_CHOICES = [
        ('', 'Select...'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    session = forms.ChoiceField(choices=SESSION_CHOICES)
    week_type = forms.ChoiceField(choices=WEEK_TYPE_CHOICES)
    day = forms.ChoiceField(choices=DAY_CHOICES)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        fields = ['day', 'session', 'week_type', 'date']