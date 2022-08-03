import pymongo

client = pymongo.MongoClient("mongodb+srv://anubhav:ar66007@anubhav.xbat2.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d={
    "name":"anubhav",
    "email":"anubhav@gmail.com",
    "surname":"kumar"
}

#print(d)

db1=client['mongodb']
coll=db1['test']
coll.insert_one(d)