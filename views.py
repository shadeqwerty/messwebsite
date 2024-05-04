from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .Processor_Codes.Processor import *
from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.contrib import messages
from django.utils.html import format_html
from .models import Review
from django.http import JsonResponse
from django.db.models import Avg
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



def logout_view(request):
    print("logging out")
    logout(request)
    messages.success(request, "Logged out successfully")

    return redirect('index')

def chart_data(request):
    labels = []
    data = []

    queryset = Review.objects.values('food_item__name').annotate(avg_rating=Avg('rating')).order_by('-avg_rating')
    for entry in queryset:
        labels.append(entry['food_item__name'])
        data.append(entry['avg_rating'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def my_view(request):
    # Get the current time, day, and session
    current_time_ist, day, session = get_current_time_session_day()
    now_time = str(current_time_ist)

    # Get the next menu item and the latest updated menu
    Next_menu_item = get_menu_items(day, session)
    latest_updated_menu, access_time = read_google_sheet_update()

    # Handle the form submission
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReviewForm()

    # Render the template
    return render(request, 'page.html', {
        'now_time': now_time,
        'Next_menu_item': Next_menu_item,
        'latest_updated_menu': latest_updated_menu,
        'access_time': access_time,
        'day': day,
        'session': session,
        'form': form,
    })

@login_required
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews')
    else:
        form = ReviewForm()

    return render(request, 'submit_review.html', {'form': form})


def reviews_viewer(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully registered!')

            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'on_register_page': True, 'form': form})