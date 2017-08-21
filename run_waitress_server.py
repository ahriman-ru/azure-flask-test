import os  
from os import environ
from waitress import serve  
from FlaskWebProject1.main import app
serve(app,host="0.0.0.0",port=os.environ["PORT"]) 