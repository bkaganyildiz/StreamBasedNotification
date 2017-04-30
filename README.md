# Stream Based Notifications

Django project that listens from redis stream and save different type of events that you can later create notifications.

### Installing

You can easily install dependencies using requirements file

```
pip install -r requirements.txt
```

### Some libraries used and their documentations 

In order to start stream : 

[Django-Channels](https://channels.readthedocs.io/en/stable/)

[Celery](http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)

In order to send notifications :

[Django-Background-Task])(http://django-background-tasks.readthedocs.io/en/latest/)



## Running the tests

In order to run : 
```
cd StreamBasedNotifs
```
```
python manage.py rumserver
```

### Some bugs that’s going to be fixed : 

- When a new event captured interface does not update itself asynchronous you have to refresh to page about 5 sec later in order to see all the events captured 

- When you load the initial page too much main thread locks and daphne gives 503 error. 

— While sending the notifications background-task lib takes the task and stored in the database which eventually does not complete the task you have to complete manually as they says in their library .

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



