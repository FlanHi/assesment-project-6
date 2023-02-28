from flask import Flask, render_template
import os

app = Flask(__name__)

picfolder=os.path.join('templates', 'static', 'images')

from app import routes