from pymongo import MongoClient

demoClient = MongoClient()
myClient = MongoClient('mongodb://localhost:27017/')
myDbConfig = myClient['mymongodb']
myCollConfig = myDbConfig['mycollection']
