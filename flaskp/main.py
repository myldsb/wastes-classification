import os

from flask import Flask


app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
	return 'hello world'

if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.run(debug=False)