from flask import Blueprint
from flask import render_template


bp = Blueprint('guide', __name__, url_prefix='/guide')

@bp.route('/', methods=('GET', 'POST'))
def guide():
	return render_template('/guide/guide.html')