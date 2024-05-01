from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .Processor_Codes.Processor import *
from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.utils.html import format_html


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

def submit_review(request):
    print("here")
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReviewForm()

    return render(request, 'submit_review.html', {'form': form})