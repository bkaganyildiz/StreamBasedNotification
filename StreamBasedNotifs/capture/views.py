from django.shortcuts import render
from django.views.decorators.csrf import  csrf_exempt #for csrf protection
from .models import Stream , Notification
from .forms import NotificationForm
from django.http import JsonResponse
# Create your views here.

@csrf_exempt
def captureEvents(request):
    '''Route to background task and display the main page'''
    streams = Stream.objects.all()
    events = {}
    for stream in streams:
        events[stream.name] = stream.info.split(',')
    form = NotificationForm(request.POST or None)
    if form.is_valid() :
        notification_name = form.cleaned_data.get("name")
        event_name = form.cleaned_data.get("event")
        target = form.cleaned_data.get("target") #if 0 user if 1 assoc. user
        delay = form.cleaned_data.get("delay")
        url = form.cleaned_data.get("url")
        if Notification.objects.filter(event_name=event_name) :
            '''If there is a notification that created for this event update it'''
            notification = Notification.objects.get(event_name=event_name)
            notification.name = notification_name
            notification.delay = delay
            notification.url = url
            if target == '0':
                notification.target = False
            else:
                notification.target = True
            #notification.target = (target =='0') ? False  : True
            notification.save()
        else:
            '''If there is no notification created for this event'''
            itarget = False
            if target == '1':
                itarget = True
            Notification.objects.create(event_name=event_name, name=notification_name,
                                        delay=delay, url=url, target=itarget)
        return render(request, "updateCapture.html", {"events": events, "form": NotificationForm()})
    return render(request, "updateCapture.html", {"events": events, "form": form})


def updateEvents(request):
    if request.method == "GET" :
        events = {}
        streams = Stream.objects.all()
        for stream in streams:
            events[stream.name] = stream.info.split(',')
        return JsonResponse(events)
    return JsonResponse({})
