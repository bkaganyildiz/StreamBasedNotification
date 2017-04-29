from django.shortcuts import render
from django.views.decorators.csrf import  csrf_exempt #for csrf protection
from channels import Channel
from .models import Stream , Notification
from .forms import NotificationForm
from django.http import JsonResponse
# Create your views here.

@csrf_exempt
def captureEvents(request) :
    '''Route to background task and display the main page'''
    #Channel('capture-stream').send({})
    form = NotificationForm(request.POST or None)
    if form.is_valid() :
        notification_name = form.cleaned_data.get("name")
        print (type(notification_name), notification_name)
        event_name = form.cleaned_data.get("event")
        print (type(event_name), event_name)
        target = form.cleaned_data.get("target") #if 0 user if 1 assoc. user
        print (type(target), target)
        delay = form.cleaned_data.get("delay")
        print (type(delay), delay)
        url = form.cleaned_data.get("url")
        print (type(url), url)
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
            if target == '1' :
                itarget = True
            Notification.objects.create(event_name=event_name, name=notification_name,
                                        delay=delay, url=url, target=itarget)
        return render(request, "capture.html", {"events": Stream.objects.all(), "form": NotificationForm()})
    return render(request, "capture.html", {"events": Stream.objects.all(), "form": form})

