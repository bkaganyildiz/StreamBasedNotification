from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect , requires_csrf_token , csrf_exempt #for csrf protection
# Create your views here.

@csrf_exempt
def captureEvents(request) :
    '''
    Call Listener class that returns json object parse it and
    send it to a template
    '''
    form = "hello"
    return render(request,"capture.html",{'form' : form , 'title' : 'Remove Key'})
