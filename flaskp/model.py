'''
return all table instance in db conn
'''


from mongoengine import *

from . import app

connect(app.config['DATABASE'])

class User(Document):
    name = StringField(required=True, max_length=16)
    password = StringField(required=True)
    group = StringField(required=True, max_length=16)

class Mall(Document):
    pass

class QuestionBank(Document):
    question = StringField(requied=True)
    options = ListField(StringField(max_length=250))
    answer = StringField(required=True)

class SystemAccessLog(Document):
    date = StringField(required=True)
    new_user = IntField(required=True)
    total_user = IntField(required=True)
    total_retention_time = IntField(required=True)
    avg_retention_time = IntField(required=True)
    total_visti_count = IntField(required=True)

class SingleRecords(EmbeddedDocument):
    operation = StringField(required=True)
    timestamp = StringField(required=True)

class UserAccessRecords(Document):
    name = StringField(required=True)
    login = StringField(required=True)
    logout = StringField(required=True)
    records = ListField(EmbeddedDocumentField(SingleRecords), required=True)
    visit = IntField(required=True)

class WasteClassfication(Document):
    name = StringField(required=True)
    category = StringField(required=True)
    version = StringField(required=True)

print([[i for i in j]  for j in WasteClassfication.objects(version='stable')])


# single_records = SingleRecords(operation = '1', timestamp = '2')
# user = UserAccessRecords(name='1234', login='1', logout='2', records=[single_records], visit=5)
# user = user.objects.create()
# user.save()



