from django.shortcuts import render, redirect
from .models import Parent, Child

def create_parent(request):
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        age = request.POST['age']
        Parent.objects.create(name=name, lastname=lastname, age=age)
        return redirect('/')
    else:
        return render(request, 'create_parent.html')

def create_child(request):
    context = {
        'parent' : Parent.objects.all()
    }
    if request.method == 'POST':
        childname = request.POST['childname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        parent_id = request.POST.get('name')
        parent = Parent.objects.get(id=parent_id)
        Child.objects.create(childname=childname, lastname=lastname, age=age, parent=parent)
        return redirect('/create_child')
    else:
        return render(request, 'create_child.html', context)
