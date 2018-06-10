import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.video
movieDetails  = db.movieDetails 

def find():
    query = {'countries.1':"Sweden"}
    selector = {'title':1}

#Executing the query
    try:
        total=movieDetails.find(query,selector).count()
        cursor = movieDetails.find(query,selector)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    sanity = 0

    print "The number of results for the query ="
    print (total)


    print "The documents in the query are "
    #Printing the document into the query
    for doc in cursor:
        print doc

#Sanity variable is used to limit the document results printed
        sanity += 1
        if (sanity > 10):
            break

find()


'''Output
The number of results for the query =
6
The documents in the query are 
{u'_id': ObjectId('5692a15024de1e0ce2dfcf73'), u'title': u'The Girl with the Dragon Tattoo'}
{u'_id': ObjectId('5692a2fc24de1e0ce2dfd83f'), u'title': u'Dallas: J.R. Returns'}
{u'_id': ObjectId('5692a3a424de1e0ce2dfd9c1'), u'title': u'If I Want to Whistle, I Whistle'}
{u'_id': ObjectId('5692a4ca24de1e0ce2dfdbdd'), u'title': u'Burma VJ: Reporter i et lukket land'}
{u'_id': ObjectId('5692a4df24de1e0ce2dfdc01'), u'title': u'Hin helgu v\xe9'}
{u'_id': ObjectId('5692a52e24de1e0ce2dfdca0'), u'title': u'Au Hasard Balthazar
'''
