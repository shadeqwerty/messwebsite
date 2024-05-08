from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
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
from .models import MenuItem
from datetime import datetime
from django.db.models import Q


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

def menu_items(request):
    import random
    from datetime import datetime
    
    if request.method == 'POST':
        day = request.POST.get('day', None)
        date = request.POST.get('date')
        session = request.POST.get('session')
        week_type = request.POST.get('week_type', 'Even')

        if date:
            print("Date selected")
            date_obj = datetime.strptime(date, '%Y-%m-%d')

            # Compute week type
            week_type = 'Odd' if date_obj.isocalendar()[1] % 2 == 1 else 'Even'

            # Compute day
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            day = days[date_obj.weekday()]
            print(day, week_type, session)
            
        else:

            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        if session != 'All':
            menu_items = MenuItem.objects.filter(day=day, week_type=week_type, session=session)
        else:
            print("All SELECTED")
            menu_items = MenuItem.objects.filter(day=day, week_type=week_type)
            print(len(menu_items))
        sessions = ['Breakfast', 'Lunch', 'Snacks', 'Dinner']
        return render(request, 'menu_items.html', {'menu_items': menu_items, 'sessions': sessions, 'days': days, 'session': session,
            'week_type': week_type,
            'day': day})
    else:
        return render(request, 'menu_items.html')
@permission_required('messwebsite.can_update_database1')
def update_database(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'update':
            week_type = request.POST.get('week_type')
            new_element = push_to_database(MenuItem, week_type)
            # add a message to the user with all new elements added
            if len(new_element) == 0:
                messages.warning(request, 'Database already up to date. No new elements added.')
            else:
                messages.success(request, format_html('Database updated successfully. Added the following elements'))
                parsed_elements = [tuple(str(elem).strip("()").split(", ")) for elem in new_element]
                messages.success(request, parsed_elements)
        elif action == 'remove':
            MenuItem.objects.all().delete()
            messages.success(request, 'All items removed from the database.')
        return redirect('update')  # Redirect to a success page after updating the database
    else:
        context = {
            'messages_items': parsed_elements if 'parsed_elements' in locals() else []
        }
        return render(request, 'update_db.html', context)  # Render the form with the context

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