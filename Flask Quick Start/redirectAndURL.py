'''
Redirect to URL
Redirect - send the user to a particular URL with status code - this status code additionally identifies the issue
access a website -> browser sends a request to the server -> server replies the HTTP status code (three-digit number)

Syntax: flask.redirect(location,code=302)

Parameters:

location(str): the location which URL directs to.
code(int): The status code for Redirect.
Code: The default code is 302 which means that the move is only temporary.

Return: The response object and redirects the user to another target location with the specified code.
'''

'''
url_for() Function
url_for(): method use when performing redirects
accepts the name of another function as the first arg
'''

from flask import Flask, redirect, url_for
app = Flask(__name__)

print('1.Redirect to URL\n2.')
i = int(input('Enter your choice: '))
match i:
    case 1:
        # home route that redirects to 
        # helloworld page
        @app.route("/")
        def home():
            return redirect("/helloworld") ### Note
        # when a user hits the base URL \ (root) it will redirect to \helloworld

        # route that returns hello world text
        @app.route("/helloworld")
        def hello_world():
            return "<p>Hello, World from \
                        redirected page.!</p>"
    
        # try: http://127.0.0.1:5000
    
    case 2:
        # decorator for route(argument) function
        @app.route('/admin')
        # binding to hello_admin call
        def hello_admin():
            return 'Hello Admin'

        @app.route('/guest/<guest>')
        # binding to hello_guest call
        def hello_guest(guest):
            return 'Hello %s as Guest' % guest

        @app.route('/user/<name>')
        def hello_user(name): # the function named user(name) accepts the value through the input URL
        
            # dynamic binding of URL to function
            # It checks whether the received argument matches the ‘admin’ argument or not. 
            # If it matches, then the function 'hello_admin()' is called else the 'hello_guest()' is called.
            if name == 'admin':
                return redirect(url_for('hello_admin'))
            else:
                return redirect(url_for('hello_guest'
                                        , guest=name))
        
        # try: http://127.0.0.1:5000/user/admin and http://127.0.0.1:5000/user/alpha


app.run()