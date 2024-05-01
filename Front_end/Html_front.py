
def generate_html(now_time, Next_menu_item, latest_updated_menu, access_time,day,session):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>C Mess Menu and Feedback</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                color: #343a40;
                margin: 0;
                padding: 0;
            }
            
            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }
            
            header {
                background-color: #007bff;
                color: #fff;
                padding: 10px 20px;
                text-align: center;
            }
            
            nav ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                text-align: center;
            }
            
            nav ul li {
                display: inline;
                margin: 0 10px;
            }
            
            nav ul li a {
                color: #fff;
                text-decoration: none;
                font-weight: bold;
                transition: color 0.3s;
            }
            
            nav ul li a:hover {
                color: #ff0;
            }
            
            .jumbotron {
                background-image: url('https://via.placeholder.com/800x400');
                background-size: cover;
                text-align: center;
                color: #fff;
                padding: 100px 20px;
            }
            
            .jumbotron h1 {
                font-size: 3em;
                margin-bottom: 20px;
            }
            
            .btn {
                display: inline-block;
                background-color: #28a745;
                color: #fff;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            
            .btn:hover {
                background-color: #218838;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>C Mess Menu and Feedback</h1>
        </header>
        """+f""" 
        <div class="container">
            <h2>Next Menu Item: {day} for {session} </h2>
            <p>{Next_menu_item}</p>
            <h2>Latest Updated Menu at {access_time}</h2>
            <p>{latest_updated_menu}</p>
        </div>"""+"""
    <div class="container">
        <h2>Review</h2>
        <form action="/submit_review" method="post">
            <label for="date">Date:</label><br>
            <input type="date" id="date" name="date" max="{today}" min="{three_days_ago}"><br>
            <label for="food_item">Food Item:</label><br>
            <input type="text" id="food_item" name="food_item"><br>
            <label for="rating">Rating (1-5):</label><br>
            <input type="number" id="rating" name="rating" min="1" max="5"><br>
            <label for="comments">Comments:</label><br>
            <textarea id="comments" name="comments"></textarea><br>
            <input type="submit" value="Submit Review">
        </form>
    </div>
       
        <footer>
            <div class="container">
                <p>&copy; 2024 No Rights are reserved as of now :P.</p>
            </div>
        </footer>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    html_content = generate_html()
    with open("fancy_website.html", "w") as file:
        file.write(html_content)
    print("HTML file generated successfully.")