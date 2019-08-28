'''
return all table instance in db conn
'''

from pymongo import MongoClient

myclient = MongoClient('mongodb://localhost:27017/')
db_conn = myclient['garbage']

# all the table instance
table_user = db_conn['user']
table_user_records = db_conn['user-records']
table_waste_classfication = db_conn['waste-classfication']
table_question_bank = db_conn['question-bank']
table_overall_records = db_conn['overall-records']
table_mall = db_conn['mall']
