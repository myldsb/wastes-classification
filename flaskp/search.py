

from flask import Blueprint, render_template, request, flash

from .model import WasteClassfication
from .help import Results

bp = Blueprint('waste-class', __name__, url_prefix='/waste-class')

@bp.route('/', methods=['POST'])
def index():
	search_name = request.form.get('waste-name')
	if not search_name:
		print(123123123123)
		flash('没有检测到输入，请输入要查询的垃圾名称')
		return render_template('index.html')
	waste_filter = ['%s[%s]'%(i.name,i.category) for i in WasteClassfication.objects(version='stable')
						   if search_name in i.name]
	print(waste_filter)
	return	render_template('/search/search.html', waste_filter=waste_filter)