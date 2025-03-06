'''
The different reasons for errors are:
- Unauthorized access or poor request.
- Unsupported media file types.
- Overload of the backend server.
- Internal hardware/connection error.

Syntax: flask.redirect(location,code=302)

Parameters:

location(str): the location which URL directs to.
code(int): The status code for Redirect.
Code: The default code is 302 which means that the move is only temporary.

Return: The response object and redirects the user to another target location with the specified code.
'''

'''
Flasks Errors
If there is an error in the address or if there is no such URL then Flask has an abort() function used to exit with an error code.

Syntax: abort(code, message)

code: int, The code parameter takes any of the following values
message: str, create your custom message Error.
'''

from flask import Flask, abort
app = Flask(__name__)

print('1.Demonstrate abort()\n2.Example 403 error')
i = int(input('Enter your choice: '))
match i:
    case 1:
        # if the username starts with a number then an error code message will through, else on success “Good username” will be printed.
        @app.route('/<uname>') 
        def index(uname): 
            if uname[0].isdigit(): 
                abort(400) 
            return '<h1>Good! %s</h1>' %uname
        
        # try: http://127.0.0.1:5000/alpha and http://127.0.0.1:5000/1alpha
    
    case 2:
        @app.route('/<uname>') 
        def index(uname): 
            if uname[0].isdigit(): 
                abort(403) 
            return f'<h1>Good {uname}</h1>'
        
        # try: http://127.0.0.1:5000/beta and http://127.0.0.1:5000/1beta

app.run()