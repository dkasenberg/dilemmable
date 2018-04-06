from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages
from main.models import Dilemma, DilemmaOption

def index(request):
    return render(request, 'index.html', {})
