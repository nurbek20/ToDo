from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from main.models import Todo
from django.http import HttpResponseNotFound
# Create your views here.
def main(request):
    todos = Todo.objects.all()
    return render(request, "index1.html", {'todos' :todos})
# Создания данных в База Данных
def create(request):
    if request.method == 'POST':
        todo=Todo()
        todo.title = request.POST.get("title")
        todo.description = request.POST.get("description")
        todo.save()
        
    return HttpResponseRedirect('/')
def error(request):
    todo=Todo.objects.all()
    return render(request, 'error.html')

def delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
        todo.delete()
        return HttpResponseRedirect('/')
    except Todo.DoesNotExist:
        return render(request, 'error.html')
def edit(request, id):
    try:
        todo = Todo.objects.get(id=id)
        if request.method == 'POST':
            todo.title = request.POST.get('title')
            todo.description = request.POST.get('description')
            todo.save()
            return HttpResponseRedirect('/')
        return render(request, 'edit.html', {'todo':todo})
    except Todo.DoesNotExist:
        return render(request, 'error.html')
# def test(request, id):
#     todos2 = Todo.objects.all()
#     return render(request, 'index1.html', {'todos2' :todos2 , 'hello':'hello', 'id':id})

def test(request, id):
    todo = Todo.objects.get(id=id)
    # print(todo)
    return render(request, 'index1.html', {'todo' :todo})

def tasks(request):
    todos = Todo.objects.all()
    return render(request, 'tasks.html', {'todos' :todos})
