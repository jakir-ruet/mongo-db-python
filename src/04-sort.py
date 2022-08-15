from pymongo import MongoClient

mgClient = MongoClient()
myClient = MongoClient('mongodb://localhost:27017/')
myDbConfig = myClient['dbMongodb']
myCollConfig = myDbConfig['myCollection']

mySort = myCollConfig.find().sort('name', 1)    # Ascending sort
# mySort = myCollConfig.find().sort('name', -1)    # Descending sort

for x in mySort:
    print(x)
