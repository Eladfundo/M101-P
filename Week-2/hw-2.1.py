import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.students
grades = db.grades

def find():
    query = {'type':'exam','score':{'$gte':65}}
    selector = {'student_id':1,'score':1}

#Executing the query
    try:
        cursor = grades.find(query,selector).sort('score',pymongo.ASCENDING).limit(10)

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
{u'student_id': 22, u'_id': ObjectId('50906d7fa3c412bb040eb5cf'), u'score': 65.02518811936324}
{u'student_id': 115, u'_id': ObjectId('50906d7fa3c412bb040eb743'), u'score': 65.47329199925679}
{u'student_id': 48, u'_id': ObjectId('50906d7fa3c412bb040eb637'), u'score': 65.71867938396781}
{u'student_id': 57, u'_id': ObjectId('50906d7fa3c412bb040eb65b'), u'score': 65.91867871499709}
{u'student_id': 87, u'_id': ObjectId('50906d7fa3c412bb040eb6d3'), u'score': 66.0470217410135}
{u'student_id': 194, u'_id': ObjectId('50906d7fa3c412bb040eb87f'), u'score': 67.09136149008972}
{u'student_id': 116, u'_id': ObjectId('50906d7fa3c412bb040eb747'), u'score': 67.09938431313856}
{u'student_id': 111, u'_id': ObjectId('50906d7fa3c412bb040eb733'), u'score': 67.16752597563053}
{u'student_id': 199, u'_id': ObjectId('50906d7fa3c412bb040eb893'), u'score': 67.33828604577803}
{u'student_id': 96, u'_id': ObjectId('50906d7fa3c412bb040eb6f7'), u'score': 67.39154510277987}
>>> 

Answer 
{u'student_id': 22, u'_id': ObjectId('50906d7fa3c412bb040eb5cf'), u'score': 65.02518811936324}


'''
