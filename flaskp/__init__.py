import os

from flask import Flask
from flask import render_template
from gevent import monkey
monkey.patch_all()

from .log import logger



app = Flask(__name__)
print("running path:===", app.root_path)

from .config import condig_obj
app.config.from_object(condig_obj)


from .auth import login_required


@app.route('/', methods=('GET', 'POST'))
@login_required
def index():
	return render_template('/index.html')

from . import records


app.register_blueprint(auth.bp)

from . import guide
app.register_blueprint(guide.bp)

from . import search
app.register_blueprint(search.bp)

from . import  exam
app.register_blueprint(exam.bp)

adppter = app.url_map.bind('localhost')
print(adppter.match('/'))
print(adppter.match('/')[0])

