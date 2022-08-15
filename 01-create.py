from pymongo import MongoClient

mgClient = MongoClient()
myClient = MongoClient('mongodb://localhost:27017/')
myDbConfig = myClient['dbMongodb']
myCollConfig = myDbConfig['myCollection']

myList = [
    {
        'id': 1,
        'name': 'Jakir',
        'email': 'jakir@gmail.com'
    }
]

x = myCollConfig.insert_many(myList)
dbList = myClient.list_database_names()
if input('Enter database ') in dbList:
    print('The database exists')
else:
    print('No database here')
print(dbList)
