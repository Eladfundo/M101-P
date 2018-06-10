import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.video
movieDetails  = db.movieDetails 

def find():
    query = {'year':2013,'rated':"PG-13",'awards.wins':0}
    selector = {'title':1}

#Executing the query
    try:
        cursor = movieDetails.find(query,selector)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    sanity = 0
#Printing the document into the query
    for doc in cursor:
        print doc

#Sanity variable is used to limit the document results printed
        sanity += 1
        if (sanity > 10):
            break

find()


'''Output
{u'_id': ObjectId('5692a3e124de1e0ce2dfda22'), u'title': u'A Decade of Decadence, Pt. 2: Legacy of Dreams'}
'''
