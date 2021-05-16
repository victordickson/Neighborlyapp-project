import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://proj2cosmosdb:21TvTDpAS4EFSVsWs4MfDE77oQsBQS8syJH06jX07QqJs0d5MWU4fFjdGICtdsrTGCM9p7KAOcpyWWseIZMHbg==@proj2cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@proj2cosmosdb@
"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['proj2db']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)