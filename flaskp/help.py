'''
useful funcs
'''

from . import app
from flask import session, request, redirect, g

class Visit:
	total_count = 0


@app.before_first_request
def visit():
	print('before_first_request=======')
	Visit.total_count += 1


class Results:

	def __init__(self):
		self.res = {}

	def get_status(self):
		return self.res['status']

	def set_res(self, staus, **kwargs):
		self.res['status'] = staus
		print(kwargs)
		for k, v in kwargs.items():
			self.res[k] = v
		return self.res

	def get_res(self):
		return self.res

