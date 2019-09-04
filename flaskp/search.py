

from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import jsonify
from flask import redirect
from flask import current_app
from urllib.parse import urlparse

from .model import WasteClassfication
from .help import Results

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
	WasteClassfication(name=request.form.get('new_waste'),
					 _class=request.form.get('waste_class'),
					 version='pending').save()
	return 'sueccess'