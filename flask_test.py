from flask import Flask

app = Flask(__name__) 
# __name__ --> this file's name "minimal"  -> Flask use it to find files 

@app.route("/")         # decorator URL "/" --> run func below
def hello_world():      # run when browser opens http://127.0.0.1:5000/
    return "<p> Helol WOrld </p>"   

@app.route("/mars")
def mars():
    return "<p> Hello Mars!! </p>"

# no route for url (ex: /venus)  --> 404 not found
# @app.route() = GET only by default -> POST to "/" -> 405 method not allowed
# each  fuc need unique name 

# run with FLASK's built in development sercer with 
# flask -- pp minimal.py run --> --app = file w/ the app run = start server
                            # --> default address = http://127.0.0.1:5000/