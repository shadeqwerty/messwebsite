import pandas as pd
import time
import pytz
import datetime

def read_google_sheet_update():
    # Construct the URL
    url = "https://docs.google.com/spreadsheets/d/1SWsaUYvRM1HMtglXUCQ6vVTKCAIYIOwnm8yY6Q9W9Ak/gviz/tq?tqx=out:csv"
    # Read the CSV data
    df = pd.read_csv(url, index_col=0)
    df.replace('\n', '<br>', regex=True, inplace=True)
    return(df['C mess Update'].loc['Items'], df['Accesed_page_at'].loc['Items'])
    return df
def get_menu_items(Day, Session):
    # read online excel sheet
    URL = "https://docs.google.com/spreadsheets/d/1tb1Y314_ybUspDj8_dMPWAla7rceSc1pSMgpf2L4J2E/gviz/tq?tqx=out:csv"
    df = pd.read_csv(URL,  index_col=0)
    df.replace('\n', '<br>', regex=True, inplace=True)
    df = df.T
    print("for day",Day)
    # Print all column names in df
    return(df[Day].loc[Session])

def get_current_time_session_day():
    # get current time and convert it to IST and then session it for breakfast, lunch, snacks or dinner
    current_time_utc = time.gmtime()
    # Convert to Indian Standard Time
    ist = pytz.timezone('Asia/Kolkata')
    current_time_ist = time.localtime(time.mktime(current_time_utc)).tm_hour + ist.utcoffset(datetime.datetime.now()).seconds//3600# df.loc[len(df.index)] = {"Day":"IST",'Breakfast':str(current_time_ist)}
    now_time = str(current_time_ist)
    # if breakfast then its 7:30 am to 10:15 am
    if current_time_ist <= 10:
        session = "Breakfast"
    # if lunch then its 12:30 pm to 2:30 pm
    elif current_time_ist <= 15:
        session = "Lunch"
    # if snacks then its 4:30 pm to 6:00 pm
    elif current_time_ist <= 18:
        session = "Snacks"
    # if dinner then its 7:30 pm to 9:15 pm
    else:
        session = "Dinner"
    # get the day from the todays
    day = time.strftime("%A")
    return(current_time_ist, day,session)
