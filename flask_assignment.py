# Q1. What is Flask Framework? What are the advantages of Flask Framework?
# Ans:

# Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.
# It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions

# Advantages:
#Easy to learn and use: Flask is a very simple framework, which makes it easy to learn and use. Even if you are new to web development, you should be able to get started with Flask quickly.

#Flexible: Flask is a very flexible framework, which means that it can be used to develop a wide variety of web applications.
#Whether you are developing a simple website or a complex web application, Flask can be used to get the job done.

#Lightweight: Flask is a very lightweight framework, which means that it does not require a lot of resources to run. 
#This makes it a good choice for developing web applications that need to be hosted on a shared hosting server.

#Active community: Flask has a very active community, which means that there are a lot of resources available to help you learn and use Flask. 
#There are also a lot of extensions available for Flask, which can be used to add additional features to your web application.



#Q2. Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in
# juypter Notebook.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == "__main__":
    app.run()
# Running



# Q3. What is App routing in Flask? Why do we use app routes?
# Ans:

# App routing in Flask is the process of mapping a URL to a function. 
# When a user visits a URL, Flask will look for a function that is associated with that URL. 
# If a function is found, Flask will call that function and return the output of the function to the user.
# We use app routes in Flask to control how users interact with our application. For example, we can use app routes to:

# Display different pages to users depending on their role.
# Allow users to perform different actions, such as creating, editing, or deleting data.
# Protect certain pages from unauthorized access.


#Q4. Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/”
#route to show the following details:
#Company Name: ABC Corporation
#Location: India
#Contact Detail: 999-444-7777

from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return  '''
    <h1>ABC Corporation</h1>
    <p>Company Name: ABC Corporation</p>
    <p>Location: India</p>
    <p>Contact Detail: 999-999-9999</p>
    '''

@app.route('/welcome')
def welcome():
    return 'welcome to ABC Corporation'

if __name__ == "__main__":
    app.run()
#running



# Q5. What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the
# url_for() function.

from flask import Flask, url_for
app = Flask(__name__)
@app.route('/')
def home():
    return 'This is the home page'
@app.route('/hello/<name>')
def hello(name):
    return 'Hello,{}'.format(name)

if __name__ == "__main__":
    url_for(home)

    



