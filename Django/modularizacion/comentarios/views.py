from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment
# Create your views here.

def test(request):

    return HttpResponse("Todo bien")

def create(request):
    #comment = Comment(name="Jose",score=5,
                   #   comment="Este es un comentario")
    
    #comment.save()

    Comment.objects.create(name="JL")

    return HttpResponse("Creando")

def delete(request):
    #comment = Comment.objects.get(id=1)
    #comment.delete()

    Comment.objects.filter(id=2).delete()

    return HttpResponse("Borrando")
