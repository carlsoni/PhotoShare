from flask import Flask
import os
import dotenv

dotenv.load_dotenv()

# build some application wide settings and create some application objects

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySuperHardKey'


# Update the imports to use the complete package name
import my_app.portal.views
import my_app.portal.models





