from django import forms
from .models import Stream


class NotificationForm(forms.Form):
    name = forms.CharField(required=True, label="Notification Name : ")
    event = forms.ChoiceField(widget=forms.Select(attrs={'class': 'select-style'}), required=True,
                              label="Event Name : ")
    target = forms.ChoiceField(required=True, choices=[(0, "User"), (1, "Associated User")],
                               widget=forms.Select(attrs={'class': 'select-style'}), label="Target : ")
    delay = forms.IntegerField(required=True, label="Delay : ")
    url = forms.URLField(label="Webhook URL : ", required=True)

    def __init__(self, *args, **kwargs):
        '''In order to update dropdown for new coming events '''
        super(NotificationForm, self).__init__(*args, **kwargs)
        choices = []
        events = Stream.objects.filter()
        for event in events:
            choices.append((event.name, event.name))
        self.fields['event'].choices = choices
