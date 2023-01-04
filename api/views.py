from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            "Endpoint" : "/news/",
            "method" : "GET",
            "body" : None,
            "description" : "Returns an array of news."
        },
        {
            "Endpoint" : "/news/id",
            "method" : "GET",
            "body" : None,
            "description" : "Returns a single news object."
        },
        {
            "Endpoint" : "/news/create/",
            "method" : "POST",
            "body" : {"body" : "_"},
            "description" : "Create new news content with data sent in post request."
        },
        {
            "Endpoint" : "/news/id/update/",
            "method" : "PUT",
            "body" : {"body" : "_"},
            "description" : "Creates an existing news with data sent in post request."
        },
        {
            "Endpoint" : "/news/id/delete/",
            "method" : "DELETE",
            "body" : None,
            "description" : "Deletes an existing news."
        },
    ]
    return Response(routes)
