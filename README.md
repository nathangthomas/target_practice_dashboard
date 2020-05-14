# Target Practice Dashboard
This is an app that accompanies the Target Practice project [HERE](https://github.com/nathangthomas/target_practice).

This project came about as a fun way to take something I was doing when taking breaks from coding and job searching (slingshot target practice) and merging it with my passion for software and interest in hardware.

###### File Structure
- run.py: This is the application's entry point. We'll run this file to start the Flask server and launch our application. Type `python3 run.py` in your terminal to spin up your local server.
- config.py: This file contains the configuration variables for your app, such as database details.
app/__init__.py: This file intializes a Python module. Without it, Python will not recognize the app directory as a module.
- app/routes.py: This file contains all the routes for our application. This will tell Flask what to display on which path.
- app/models.py: This is where the models are defined. A model is a representation of a database table in code.

#### Useful Links
- [Setting up SQLite DB in Flask](https://www.youtube.com/watch?v=cYWiDiIUxQc)

###### SQLite Database Commands
`python3`
`from models import db`
`db.create_all()`
`from models import User, Shot`
`user_1 = User(username='Nathan', email='nathan.gordon.thomas@gmail.com', password='password')`
`db.session.add(user_1)`
`db.session.commit()`
`User.query.all()`
`User.query.first()`
`User.query.filter_by(username='Nathan').all()`
`user = User.query.filter_by(username='Nathan').first()`
`user.id`
`User.query.get(1)`
`shot_2\1 = Shot(hit=True, user_id=1)`
`db.session.add(shot_1)`
`db.session.commit()`
`user.shots`
`db.drop_all()`
`db.create_all()`
