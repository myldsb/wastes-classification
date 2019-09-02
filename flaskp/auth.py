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
from werkzeug.security import check_password_hash, generate_password_hash

from .model import User
from .help import Results


bp = Blueprint('auth', __name__, url_prefix='/auth')	


@bp.route('/', methods=['GET','POST'])
def login():
	res = Results()
	db_auth = {u.name: u.password for u in User.objects.all()}
	print('db_auth', db_auth)
	if request.method == 'POST':
		print(request.form)
		username = request.form['username']
		password = request.form['password']
		is_login = True if request.form['islogin'] == 'Login' else False

		if is_login:
			# login
			if username not in db_auth:
				flash('用户不存在，请先注册或者核实后重新登录')
			elif not check_password_hash(db_auth[username], password):
				flash('用户名或者密码错误，请核实后重新输入')
			else:
				session['username'] = username
				session['password'] = password
				g.username = username
				return redirect(url_for('index'))
		else:
			# register
			if username not in db_auth:
				print(username, password)
				try:
					User(name=username, password=generate_password_hash(password), group=current_app.config['GUEST_GROUP']).save()
					flash('注册成功，请登录')
				except Exception as e:
					print(e)
					flash('注册失败，请联系管理员')
			else:
				flash('用户名已存在，请重新输入')

	return	render_template('/auth/auth.html')


@bp.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('auth.login'))


def login_required(view):
	print('login_required')
	print('view function', view.__name__)
	@functools.wraps(view)
	def wrapped_view(*args, **kwargs):
		print('login_required=====')
		if 'username' not in session:
			return redirect(url_for('auth.login'))
		return view(*args, **kwargs)
	return wrapped_view

