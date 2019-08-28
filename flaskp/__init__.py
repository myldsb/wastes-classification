import os
from flask import Flask, render_template, url_for


app = Flask(__name__)
print("running path:===", app.root_path)


@app.route('/', methods=('GET', 'POST'))
def index():
	return render_template('index.html')

# db conn
from .db_conn import *

from . import help

from . import records

from . import auth
app.register_blueprint(auth.bp)

from . import guide
app.register_blueprint(guide.bp)

from . import search
app.register_blueprint(search.bp)

from . import  exam
app.register_blueprint(exam.bp)

