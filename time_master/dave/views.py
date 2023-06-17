# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from dave.models import Band
from django.shortcuts import render

def dave(request):
    bands = Band.objects.all()
    return render(request, 
                  'dave/dave.html',
                  {'bands': bands})