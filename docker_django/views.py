from django.http import HttpResponse
from django.shortcuts import render
from . import mongo_client
import pymongo

def home(request):
    db = mongo_client['attackflow']
    collections = db.list_collection_names()
    return render(request, 'home.html', context={'db':collections})
