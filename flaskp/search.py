'''
search waste and other related funcs
'''

import inspect

from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import jsonify
from flask import redirect
from flask import current_app
from flask import session
from urllib.parse import urlparse

from .model import WasteClassfication, User
from .help import Results
from .log import logger

bp = Blueprint('waste-class', __name__, url_prefix='/waste-class')


@bp.route('/', methods=['GET', 'POST'])
def index():
	'''
	the view func of searching
	:return:
	'''
	if request.method == 'POST':
		search_name = request.form.get('waste-name')
		if not search_name:
			flash('没有检测到输入，请输入要查询的垃圾名称')
			# get the source url
			from_url = urlparse(request.referrer).path
			# get the view func with the from_url
			adapter = current_app.url_map.bind('localhost')
			print(adapter.match(from_url)[0])
			# return the view of the source url of the request
			return redirect(url_for(adapter.match(from_url)[0]))
		else:
			# get the list that include the waste-name from front-end
			# eg:['西瓜霜[有害垃圾]'， ‘西瓜皮[厨余垃圾]’]
			waste_filter = ['%s[%s]'%(i.name,i.category) for i in WasteClassfication.objects(version='stable')
								   if search_name in i.name]
			print(waste_filter)
			return	render_template('/search/search.html', waste_filter=waste_filter)
	else:
		return render_template('/search/search.html', waste_filter=None)


@bp.route('/new_waste', methods=['POST'])
def new_waste():
	# new a waste classfication record
	print(request.form)
	res = Results()
	try:
		WasteClassfication(name=request.form.get('new_waste'),
						 category=request.form.get('waste_class'),
						 version='pending',
						 user=session['username']).save()
		return res.set_res(True, msg='添加成功，等待管理员合入')
	except Exception as e:
		logger.error(inspect.stack()[1][3])
		return res.set_res(False, msg='添加失败，请联系管理员')


@bp.route('/notification')
def notification():
	login_user = session['username']
	if login_user in [i.name for i in User.objects(group='admin')]:
		print(1)
		data = ['%s[%s]  提交者：%s'%(i.name,i.category,i.user) for i in WasteClassfication.objects(version='pending')]
	else:
		print(2)
		data = ['%s[%s]'%(i.name,i.category) for i in WasteClassfication.objects(version='pending',
																				user=session['username'])]
	print(data)
	return render_template('/search/notification.html', merge_notification=data)


@bp.route('/merge-agreement')
def merge_agreement():
	# merge the merge requests
	res = Results()
	if session.get('username') != 'admin':
		res.set_res(False, msg='你没有merge权限，请联系管理员')
	else:
		WasteClassfication.objects(version='pending').update(version='stable')
		res.set_res(True, msg='合入成功')
	return res.get_res()


@bp.route('/merge-rejecttion')
def merge_rejection():
	# reject the mrege requests
	res = Results()
	if session.get('username') != 'admin':
		res.set_res(False, msg='你没有reject权限，请联系管理员')
	else:
		WasteClassfication.objects(version='pending').delete()
		res.set_res(True, msg='删除成功')
	return res.get_res()


