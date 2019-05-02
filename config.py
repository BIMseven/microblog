import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    """ The Flask-SQLAlchemy extension takes the location of the application's 
        database from the SQLALCHEMY_DATABASE_URI configuration variable [...]
        taking the database URL from the DATABASE_URL environment variable, 
        and if that isn't defined, I'm configuring a database named app.db located 
        in the main directory of the application, which is stored in the basedir 
        variable. """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
        
    """ The SQLALCHEMY_TRACK_MODIFICATIONS configuration option is set to False to 
        disable a feature of Flask-SQLAlchemy that I do not need, which is to signal
        the application every time a change is about to be made in the database. """
    SQLALCHEMY_TRACK_MODIFICATIONS = False