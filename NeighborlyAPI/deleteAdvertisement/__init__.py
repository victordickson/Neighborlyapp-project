import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://proj2cosmosdb:21TvTDpAS4EFSVsWs4MfDE77oQsBQS8syJH06jX07QqJs0d5MWU4fFjdGICtdsrTGCM9p7KAOcpyWWseIZMHbg==@proj2cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@proj2cosmosdb@"
 # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['proj2appdb']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
