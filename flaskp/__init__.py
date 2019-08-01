import os
from flask import Flask, render_template, url_for


def init_app():
	app = Flask(__name__)
	print("running path:===", app.root_path)


	@app.route('/', methods=('GET', 'POST'))
	def index():
		return render_template('index.html')

	from . import auth
	app.register_blueprint(auth.bp)

	from . import guide
	app.register_blueprint(guide.bp)

	return app