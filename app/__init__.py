from flask import Flask

# it is in this file that we create/initialize flask object, 
# all view fns with @ decorator will be imported here.
app = Flask(__name__)

from app import views