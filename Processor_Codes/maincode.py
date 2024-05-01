import pandas as pd
from .Processor import *
from .html_maker import *
from ..Front_end.Html_front import *
def hmtl_synth():
    current_time_ist, day,session =  get_current_time_session_day()
    Next_menu_item = get_menu_items(day, session)
    print(Next_menu_item)

    latest_updated_menu, access_time = read_google_sheet_update()
    print("latest_item", latest_updated_menu,"Acccesd at \n",access_time)

    now_time = str(current_time_ist)

    #html_made = html_made.replace('&lt;br&gt;', '<br>')
    html_made = generate_html(now_time, Next_menu_item, latest_updated_menu, access_time ,day,session)
    with open('messwebsite/templates/index2.html', 'w',encoding='utf-8') as f:
        f.write(html_made)
