'''
GET method in Flask
GET: request data from a sever
The 'squarenum.html' file allows user to enter a number. Data is sent to the same page as indicated by '#'
Because of GET method, the data will be append to URL
'''
'''
POST method in Flask
POST: send data from client to sever
'''
# import the Flask library
from flask import Flask, render_template, request


# Create the Flask instance and pass the Flask 
# constructor the path of the correct module
app = Flask(__name__)


print('1.GET method\n2.POST method\n')
i = int(input('Enter your choice: '))
match i:
    case 1:

        # The URL  localhost:5000/square is mapped to
        # view function 'squarenumber'
        # The GET request will display the user to enter 
        # a number (coming from squarenum.html page)
        # answermaths method

        @app.route('/square', methods=['GET'])
        def squarenumber():
            # If method is GET, check if  number is entered 
            # or user has just requested the page.
            # Calculate the square of number and pass it to 
            if request.method == 'GET':
           # If 'num' is None, the user has requested page the first time
                if(request.args.get('num') == None):
                    return render_template('squarenum.html')
                  # If user clicks on Submit button without 
                  # entering number display error
                elif(request.args.get('num') == ''):
                    return "<html><body> <h1>Invalid number</h1></body></html>"
                else:
                  # User has entered a number
                  # Fetch the number from args attribute of 
                  # request accessing its 'id' from HTML
                    number = request.args.get('num')
                    sq = int(number) * int(number)
                    # pass the result to the answer HTML
                    # page using Jinja2 template
                    return render_template('answer.html', 
                                           squareofnum=sq, num=number)

        # try: http://localhost:5000/square

    case 2:
        @app.route('/', methods=['GET', 'POST'])
        def squarenumber():
         # If method is POST, get the number entered by user
         # Calculate the square of number and pass it to answermaths 
            if request.method == 'POST':
                if(request.form['num'] == ''):
                    return "<html><body> <h1>Invalid number</h1></body></html>"
                else:
                    number = request.form['num']
                    sq = int(number) * int(number)
                    return render_template('answer.html', 
                                    squareofnum=sq, num=number)
            # If the method is GET,render the HTML page to the user
            if request.method == 'GET':
                return render_template("squarenum.html")



# Start with flask web app with debug as
# True only if this is the starting page
if(__name__ == "__main__"):
    app.run()
