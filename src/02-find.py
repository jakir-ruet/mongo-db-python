from pymongo import MongoClient

mgClient = MongoClient()
myClient = MongoClient('mongodb://localhost:27017/')
myDbConfig = myClient['dbMongodb']
myCollConfig = myDbConfig['myCollection']

# x = myCollConfig.find_one()
# print(x)

for x in myCollConfig.find():
    print(x)
