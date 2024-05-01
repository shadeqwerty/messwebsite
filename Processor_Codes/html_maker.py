import datetime

def make_good_looking_website(df,now_time):
    # Convert DataFrame to HTML

    html = df.to_html()
    
    # Add CSS and HTML
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        .table-container, .update-container {{
            border: 2px solid black;
            padding: 10px;
            width: 90%;
            margin: auto;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }}
        @media screen and (max-width: 600px) {{
            table, th, td {{
                width: 100%;
                display: block;
            }}
        }}
        .marquee {{
            width: 100%;
            overflow: hidden;
            border: 1px solid black;
        }}
        </style>
    </head>
    <body>
        <h1>Welcome User!</h1>
        <div class="marquee">
            <marquee>Current time: {now_time}</marquee>
        </div>
        <div class="table-container">
            {html}
        </div>
    </body>
    </html>
    '''
    
    return html
    