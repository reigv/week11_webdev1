from flask import Flask          # import Flask class

app = Flask(__name__)            # create app = web server

@app.route("/")                  # URL "/" = home page
def home():                      # http://127.0.0.1:5000/
    return "<h1>Welcome to My Website!</h1>"     # <h1> = big heading

@app.route("/about")             # URL "/about"
def about():                     # http://127.0.0.1:5000/about
    return "<p>This is a simple Flask application.</p>"   # <p> = paragraph

@app.route("/contact")           # URL "/contact"
def contact():                   # http://127.0.0.1:5000/contact
    return "<h1>Contact Us</h1><p>contact@example.com</p>"  # 1 return, multiple HTML tags

# 3 routes -> 3 URLs -> 3 functions
# each function = unique name
# URL case-sensitive -> /About -> 404
# no trailing slash -> /about/ -> 404

# run with Flask's built-in development server with:
# flask --app mult_routes.py run

# 127.0.0.1 - - [19/Nov/2026 13:54:40] "GET / HTTP/1.1" 200 -
#     |             |                   |  |    |       |
#     |             |                   |  |    |       status code  (200 meanOK and 404 mean noroute)
#     |             |                   |  |    HTTP version
#     |             |                   |  URL you asked for
#     |             |                   HTTP method
#     |             date + time of the request
#     who sent it (127.0.0.1 = your own computer)