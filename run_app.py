
from flaskp import init_app

if __name__ == '__main__':
	app = init_app()
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(debug=True)
# 	