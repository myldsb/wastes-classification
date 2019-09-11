'''
user records and overall records
'''

from . import app

@app.before_request
def visit_record():
	# add the visit record when there is a visit
	pass