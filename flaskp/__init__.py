import os

from flask import Flask, render_template, url_for


app = Flask(__name__)
print(app.root_path)


@app.route('/', methods=('GET', 'POST'))
def index():
	return render_template('base.html')

@app.route('/introduce', methods=('GET', 'POST'))
def introduce():
	return render_template('/introduce/introduce.html')

if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.run(debug=False)