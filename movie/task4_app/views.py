from django.shortcuts import render, redirect

import task4_app
from .forms import Task4_form
from .models import Task4


# Create your views here.
def index(request):
    task4 = Task4.objects.all()
    return render(request, 'index.html', {'task': task4})


def detail(request, task4_id):
    task4 = Task4.objects.get(id=task4_id)
    return render(request, 'detail.html', {'task4': task4})


def add(request):
   if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        image = request.FILES['image']
        task4 = Task4(name=name, desc=desc, image=image)
        task4.save()
        return redirect('/')
   return render(request, 'add.html',)


def edit(request, id):
    task4 = Task4.objects.get(id=id)
    form = Task4_form(request.POST or None, request.FILES,instance=task4)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'task4': task4,'form':form})


def delete(request,id):
    if request.method == 'POST':
        task4 = Task4.objects.get(id=id)
        task4.delete()
        return redirect('/')
    return render(request, 'delete.html')
