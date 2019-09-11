
from flaskp import app
from gevent import pywsgi

if __name__ == '__main__':
	# app = init_app()
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.debug = True
	server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
	server.serve_forever()