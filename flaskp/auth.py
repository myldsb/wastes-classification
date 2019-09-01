'''
auth and register
'''

import functools

from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import g
from flask import jsonify
from flask import session
from flask import redirect
from flask import url_for
from flask import current_app

from .model import user, User
from .help import Results


bp = Blueprint('auth', __name__, url_prefix='/auth')	


@bp.route('/', methods=['GET','POST'])
def login():
	res = Results()
	db_auth = {u.name: u.password for u in user}
	if request.method == 'POST':
		print(request.form)
		username = request.form['username']
		password = request.form['password']
		is_login = True if request.form['islogin'] == 'Login' else False

		if is_login:
			# login
			print(111)
			print(db_auth)
			if username not in db_auth:
				flash('用户名错误或者不存在')
				# return res.set_res(False, msg='Incorrect username, please recheck')
			elif password != db_auth[username]:
				print(222)
				return res.set_res(False, msg='Incorrcet password, please recheck')
			else:
				print(333)
				session['username'] = username
				session['password'] = password
				g.username = username
				return redirect(url_for('index'))
		else:
			# register
			if username not in db_auth:
				User(name=username, password=password, group=current_app.config['GUEST_GROUP']).save()
				# return res.set_res(True, msg={'username':username, 'password':password})
				flash('注册成功')
			else:
				return res.set_res(False, msg='username already exists, please reenter')

	return	render_template('/auth/auth.html')


@bp.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('auth.login'))



def login_required(view):
	print('login_required')
	print('view', view.__name__)
	@functools.wraps(view)
	def wrapped_view(*args, **kwargs):
		print('login_required=====')
		if 'username' not in session:
			return redirect(url_for('auth.login'))
		return view(*args, **kwargs)
	return wrapped_view

