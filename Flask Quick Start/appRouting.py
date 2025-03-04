"""
App Routing: map the URL to a specific function - handle the logic for that URL
To bind a function to an URL path we use the app.route 
"""

'''
Dynamic URLs: by using variables in URL. 
Adding variables to URLs by using <variable_name> rule
We can also convert the variable to specific data type (default is set to string), use <converter: variable>
''' 

"""
add_url_rule() function: also use to mapping URL
Used in case import view function in other module
app.route call this fuction internally
Syntax: add_url_rule(<url rule>, <endpoint>, <view function>) 
"""

from flask import Flask 
  
app = Flask(__name__) 

print('1.Example\n2.Dynamic URLs\n3.Convert variable\n4.add_url_rule() function')

i = int(input("Enter your choice: "))

match i:
    case 1:
        # Pass the required route to the decorator. 
        @app.route("/hello") 
        def hello(): 
            return "Hello, Welcome to GeeksForGeeks"
        # The hello function is now mapped with '/hello' path    
        # The URL('/') is associated with the root URL.
        @app.route("/")
        def index(): 
            return "Homepage of GeeksForGeeks"

        if __name__ == "__main__": 
            app.run() 

    case 2:
        @app.route('/user/<username>') 
        def show_user(username): 
            # Greet the user 
            return f'Hello {username} !'

        @app.route("/") 
        def index(): 
            return "Homepage of GeeksForGeeks"

        if __name__ == "__main__": 
            app.run()
        
        # try: http://127.0.0.1:5000 and http://127.0.0.1:5000/user/alpha

    case 3:
        @app.route('/post/<int:id>') 
        def show_post(id): 
            # Shows the post with given id. 
            return f'This post has the id {id}'

        if __name__ == "__main__": 
            app.run()
        
        # try: http://127.0.0.1:5000/post/12

    case 4:
        def show_user(username): 
        # Greet the user 
            return f'Hello {username} !'
    
        app.add_url_rule('/user/<username>', 'show_user', show_user) 

        if __name__ == "__main__": 
            app.run()
        
        # try: http://127.0.0.1:5000/user/alpha