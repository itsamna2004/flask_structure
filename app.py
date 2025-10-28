##Assignment
# Create an app in Flask ,then perform following tasks in your app
# 1.Create a new route /hello/<username> that greets the user by name using a Jinja2 template.


# from flask import Flask, render_template, requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name='Amna')


# # /square/<int:number> - Returns the square of the number


@app.route('/square/<int:number>')
def square(number):
    return f"The square of {number} is {number * number}"


# # /repeat/<string:word>/<int:times> - Repeats the word specified times

@app.route('/repeat/<string:word>/<int:times>')
def repeat(word, times):
    return f"{word}" * times
###done


# # Add another route /info that displays current date and time.

from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Homepage!"

@app.route('/info')
def info():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"Current Date and Time: {current_time}"

if __name__ == '__main__':
    app.run(debug=True)
    ##done
    
# # Style your HTML page using basic CSS.

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def signup():
    return '''
    <html>
    <head>
        <title>Signup</title>
        <style>
            body {font-family: Arial; background: #f2f2f2; text-align: center;}
            form {background: #fff; padding: 20px; margin: 100px auto; width: 300px;
                  border-radius: 10px; box-shadow: 0 0 10px gray;}
            input {width: 90%; padding: 8px; margin: 8px 0;}
            input[type=submit] {background: green; color: white; border: none; cursor: pointer;}
            input[type=submit]:hover {background: darkgreen;}
        </style>
    </head>
    <body>
        <h2>Signup Form</h2>
        <form action="/submit" method="POST">
            <input type="text" name="name" placeholder="Name" required><br>
            <input type="email" name="email" placeholder="Email" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <input type="submit" value="Signup">
        </form>
    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    return f'''
    <html>
    <head>
        <title>Submitted</title>
        <style>
            body {{font-family: Arial; background: #fafafa; text-align: center; padding: 50px;}}
            div {{background: #fff; display: inline-block; padding: 20px; border-radius: 10px;
                 box-shadow: 0 0 10px gray;}}
            a {{text-decoration: none; color: white; background: green; padding: 8px 12px;
                border-radius: 5px; display: inline-block; margin-top: 10px;}}
            a:hover {{background: darkgreen;}}
        </style>
    </head>
    <body>
        <div>
            <h2>Signup Successful!</h2>
            <p><b>Name:</b> {name}</p>
            <p><b>Email:</b> {email}</p>
            <p><b>Password:</b> {password}</p>
            <a href="/">Go Back</a>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

##done

##Assignment no. 2

# Create a login form with username and password fields.
# If both fields are filled, display a welcome message.
# If any field is empty, display an error message.
# Create a feedback form with name, email, and message fields.
# On submission, show all entered data back on the browser.

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def signup_form():
    return '''
        <h2>Signup Form</h2>
        <form action="/submit" method="POST">
            Name: <input type="text" name="name"><br><br>
            Email: <input type="email" name="email"><br><br>
            Password: <input type="password" name="password"><br><br>
            <input type="submit" value="Signup">
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit_data():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    return f'''
        <h2>Signup Successful!</h2>
        <p><b>Name:</b> {name}</p>
        <p><b>Email:</b> {email}</p>
        <p><b>Password:</b> {password}</p>
        <a href="/">Go Back</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
    ###done

