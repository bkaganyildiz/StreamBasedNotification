from django.shortcuts import render
from django.views.decorators.csrf import  csrf_exempt #for csrf protection
from channels import Channel
from .models import Stream
import redis
from django.http import JsonResponse
# Create your views here.

@csrf_exempt
def captureEvents(request) :
    '''
    Route to background task and display the main page
    '''
    Channel('capture-stream').send({})
    return render(request,"capture.html",{"events": Stream.objects.all()})

