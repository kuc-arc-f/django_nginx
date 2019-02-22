#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView

# Create your views here.
from django.http import HttpResponse
from django.template import loader


# Create your views here.
#
def index(request):
    return HttpResponse('Hello World ,from test1')
