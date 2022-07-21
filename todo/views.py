from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo


def home(request):
    # obj = Todo.objects.all()
    obj = Todo.objects.order_by('-added_date')
    context = {'todos': obj}
    return render(request, 'todo/index.html', context)


def todo(request):
    text = request.POST['content']
    Todo.objects.create(text=text)
    return redirect('home')


def delete(request, id):
    obj = get_object_or_404(Todo, id=id)
    obj.delete()
    return redirect('home')
