# MicoBlog

First use of the flask-migrate module. Using it to help housekeep the database, locate it in the 4th parth of the Ultimate flask tutorial
changes to the db can be applied to the entire application with the commands:
    flask db migrate -m "message" # creates a migrate
    flask db upgrade # applies it to the database