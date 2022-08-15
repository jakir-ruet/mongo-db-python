from pymongo import MongoClient

mgClient = MongoClient()
myClient = MongoClient('mongodb://localhost:27017/')
myDbConfig = myClient['dbMongodb']
myCollConfig = myDbConfig['myCollection']

myQuery = {
    'name': 'Jakir'
}

result = myCollConfig.find(myQuery)
for x in result:
    print(x)
