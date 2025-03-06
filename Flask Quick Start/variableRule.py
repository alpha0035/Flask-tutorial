'''
Flask-Variable Rules:
- Creating dynamic URL by adding variable part
- Define variable rule by <variable-name>
- Variable is always passed as a keyword argument to the function
'''

from flask import Flask
app = Flask(__name__)

print('1.Simple example\n2.Variable Type\n3.Multiply variable\n4.Default variable\n')
i = int(input('Enter your choice: '))
match i:
    case 1:
        @app.route('/')
        def msg():
            return "Welcome To The GreeksForGreeks"
    case 2:
        @app.route('/user/<username>')
        def msg(username):
            return f'Hello boss! {username}'
        # try: http://127.0.0.1:5000/user/alpha
        
        @app.route('/type/<int:type>')
        def msg2(type):
            return f'Your type is {type*type}'
        
        # try: http://127.0.0.1:5000/type/14
        
        @app.route('/rate/<float:rate>')
        def msg3(rate):
            return f'Your rate is {rate*100}%'
        
        # try: http://127.0.0.1:5000/rate/0.43

    case 3:
        @app.route('/mySever/<name>/<int:type>/<float:rate>')
        def msg(name, type, rate):
            return f'Hello alpha-{name}\nYour type is {type*type}\nWith rating {rate*100}%'
        
        # try: http://127.0.0.1:5000/mySever/AnhKy/3/0.38

    case 4:
        @app.route('/hello/')
        @app.route('/hello/<name>')
        def msg(name = 'Guest'):
            return f'Hello {name}'
        
        # try: http://127.0.0.1:5000/hello and http://127.0.0.1:5000/hello/Alpha
app.run()