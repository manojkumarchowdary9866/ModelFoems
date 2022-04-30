from django.http import HttpResponse
from django.shortcuts import render

from app.forms import topicForm
from app.forms import *

# Create your views here.
def insert_topic(request):
    FO=topicForm()
    d={'FO':FO}
    if request.method=='POST':
        FD=topicForm(request.POST)
        if FD.is_valid():

            FD.save()
        return HttpResponse('insert data')


    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    FO=webpageForm()
    d={'FO':FO}
    if request.method=='POST':
        FD=webpageForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('Webapage inserted')

    return render(request,'insert_webpage.html',d)


