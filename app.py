#Import flask dependency
from flask import Flask
#Create a flask app instance 
#An instance is a singular version of the thing in use 
app = Flask(__name__)
#The double underscores indicate that these variables are magic or dunder methods
"""Here __name__ is used to denote the name of current function. It is used to determine
  whether a file is being directly run or is imported from another module.  If run directly __name__ is 
  given the value: '__main__' ; if run as an import then __name__ is given the name of the imported file """

#Create a route:
@app.route('/')     
#The single forward slash specified we are in the root 
def hello_world():
    return 'Hello World' 

"""We can then save this and export it as an environment variable """