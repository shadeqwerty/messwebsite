import pandas as pd
import time
import pytz
import datetime
from ..models import MenuItem
from datetime import datetime


def push_to_database(Model, week_type):
    df = generate_databse(week_type)
    DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    SESSIONS = ['Breakfast', 'Lunch', 'Snacks', 'Dinner']
    model_instances = []
    new_elements = []

    for day in DAYS:
        for session in SESSIONS:
            # Extract the string of food items
            food_items_str = df[day].loc[session]
            # Split the string of food items by comma into a list
            food_items_list = food_items_str.split(',')
            # Remove any leading or trailing spaces from each food item in the list
            food_items_list = [item.strip() for item in food_items_list]
            # For each food item, create a new instance of the Django model
            for food_item in food_items_list:
                # Check if an instance with the same attributes already exists in the database
                exists = Model.objects.filter(day=day, session=session, week_type=week_type, food_item=food_item).exists()
                if not exists:
                    model_instance = Model(day=day, session=session, week_type=week_type, food_item=food_item)
                    model_instances.append(model_instance)
                    new_elements.append((day, session, week_type, food_item))

    # Use Django's bulk_create method to insert all the model instances into the database at once
    Model.objects.bulk_create(model_instances)

    return new_elements

def read_google_sheet_update():
    # Construct the URL
    url = "https://docs.google.com/spreadsheets/d/1SWsaUYvRM1HMtglXUCQ6vVTKCAIYIOwnm8yY6Q9W9Ak/gviz/tq?tqx=out:csv"
    # Read the CSV data
    df = pd.read_csv(url, index_col=0)
    df.replace('\n', '<br>', regex=True, inplace=True)
    return(df['C mess Update'].loc['Items'], df['Accesed_page_at'].loc['Items'])
    return df


def generate_databse(week_type):
    if week_type == "Odd":
        oddweek_URL ="https://docs.google.com/spreadsheets/d/1O3xKZPQVhSlvTAO1loZIhtkPxYcDg5eWBo1J5WeiiBc/gviz/tq?tqx=out:csv"
        df = pd.read_csv(oddweek_URL,  index_col=0)
        df.replace('\n', '<br>', regex=True, inplace=True)
        df = df.T
    elif week_type == "Even":
        evenweek_URL = "https://docs.google.com/spreadsheets/d/1tb1Y314_ybUspDj8_dMPWAla7rceSc1pSMgpf2L4J2E/gviz/tq?tqx=out:csv"
        df = pd.read_csv(evenweek_URL,  index_col=0)
        df.replace('\n', '<br>', regex=True, inplace=True)
        df = df.T
    return(df)


def get_menu_items(current_time_ist, day, session):
    # get date
    date = time.strftime("%Y-%m-%d")
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    # Compute week type
    week_type = 'Odd' if date_obj.isocalendar()[1] % 2 == 1 else 'Even'
    menu_items = MenuItem.objects.filter(day=day, session=session, week_type=week_type)
    # Convert the QuerySet to a DataFrame
    df = pd.DataFrame.from_records(menu_items.values())
    print(menu_items)
    return menu_items

def get_current_time_session_day():
    # get current time and convert it to IST and then session it for breakfast, lunch, snacks or dinner
    current_time_utc = time.gmtime()
    # Convert to Indian Standard Time
    ist = pytz.timezone('Asia/Kolkata')
    current_time_ist = time.localtime(time.mktime(current_time_utc)).tm_hour + ist.utcoffset(datetime.now()).seconds//3600# df.loc[len(df.index)] = {"Day":"IST",'Breakfast':str(current_time_ist)}
    now_time = str(current_time_ist)
    print(current_time_ist)
    day = time.strftime("%A")
    # if breakfast then its 7:30 am to 10:15 am
    if current_time_ist <= 10:
        session = "Breakfast"
    # if lunch then its 12:30 pm to 2:30 pm
    elif current_time_ist < 13:
        session = "Lunch"
    # if snacks then its 4:30 pm to 6:00 pm
    elif current_time_ist < 18:
        session = "Snacks"
    # if dinner then its 7:30 pm to 9:15 pm
    elif current_time_ist < 22:
        session = "Dinner"
    else:
        session = "Breakfast"
        # change the day to tomorrow
        if day == "Monday":
            day = "Tuesday"
        elif day == "Tuesday":
            day = "Wednesday"
        elif day == "Wednesday":
            day = "Thursday"
        elif day == "Thursday":
            day = "Friday"
        elif day == "Friday":
            day = "Saturday"
        elif day == "Saturday":
            day = "Sunday"
        elif day == "Sunday":
            day = "Monday"
    # get the day from the todays
    print(session, day, current_time_ist)
    return(current_time_ist, day,session)
