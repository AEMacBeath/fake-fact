from django import forms
from .models import Message


# Message Form
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('body',)
