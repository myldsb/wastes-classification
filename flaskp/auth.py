'''
auth and register
'''


from flask import Blueprint, render_template, request, flash, g, jsonify

from .db_conn import *
from .help import Results


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/', methods=['GET','POST'])
def index():
	res = Results()
	auth = {i['name']: i['password'] for i in table_user.find()}
	if request.method == 'POST':
		print(request.form)
		username = request.form['username']
		password = request.form['password']
		is_login = True if request.form['islogin'] == 'Login' else False

		if is_login:
			if username not in auth:
				return res.set_res(False, msg='Incorrect username, please recheck')
			elif password != auth['username']:
				return res.set_res(False, msg='Incorrcet password, please recheck')
			else:
				return res.set_res(True)
		else:
			if username not in auth:
				return res.set_res(True, msg={'username':username, 'password':password})
			else:
				return res.set_res(False, msg='username already exists, please reenter')

	return	render_template('/auth/auth.html')