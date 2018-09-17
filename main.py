from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """ 
<!doctype html>
    <html>
        <head></head>
        <body>
            <form action="/hello" method="post">
                <label for="first-name">First Name</label>
                <input id="first-name" type="text" name="firstName" />
                <input type="submit" />
            </form>
        </body>
    </html>
"""


@app.route("/")
def index():
    return form


@app.route("/hello", methods=['POST'])
def hello():
    firstName = request.form['firstName']
    return '<h1>Hello, ' + firstName + '<h1>'


app.run()
