from pyexpat import model
from django import forms
from app.models import *
class topicForm(forms.ModelForm):
    class Meta:
        model=topic
        fields='__all__'
class webpageForm(forms.ModelForm):
    class Meta:
        model=webpage
        fields='__all__'
    
