from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note


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

@api_view(["GET"])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getNote(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data["body"]
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(["PUT"])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(["DELETE"])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note was deleted!")
