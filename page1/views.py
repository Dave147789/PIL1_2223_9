from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    context = {"message": "Hello world !"}
    template = loader.get_template("page1/index.html")
    return HttpResponse(template.render(context, request))
