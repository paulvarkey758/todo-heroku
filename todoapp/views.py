from django.shortcuts import render
from django.http import HttpResponse
from .models import Todolist

# Create your views here.
def mainfun(requests):
    t=Todolist.objects.all()
    return render(requests,"index.html",{'tasks':t})

def get_data(requests):
       data=requests.POST['task'] 
       nt=Todolist(task=data)
       nt.save()
       t=Todolist.objects.all()
       return render(requests,"index.html",{'tasks':t})

def del_data(requests,task_id):
       dt=Todolist.objects.get(id=task_id)
       dt.delete()
       t=Todolist.objects.all()
       return render(requests,"index.html",{'tasks':t})
