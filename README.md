###### File Structure
run.py: This is the application's entry point. We'll run this file to start the Flask server and launch our application. Type `python run.py` in your terminal to spin up your local server.
config.py: This file contains the configuration variables for your app, such as database details.
app/__init__.py: This file intializes a Python module. Without it, Python will not recognize the app directory as a module.
app/views.py: This file contains all the routes for our application. This will tell Flask what to display on which path.
app/models.py: This is where the models are defined. A model is a representation of a database table in code. However, because we will not be using a database in this tutorial, we won't be needing this file.
