from flask import Blueprint, render_template


bp = Blueprint('exam', __name__, url_prefix='/exam')

@bp.route('/', methods=('GET', 'POST'))
def exam():
	return render_template('/exam/exam.html')