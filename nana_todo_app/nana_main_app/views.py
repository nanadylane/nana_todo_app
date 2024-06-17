from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


# from django.contrib.auth.forms import RegistrationForm


from .models import *
from .forms import *

@login_required
def index(request):
    tasks = NanaTask.objects.filter(owner = request.user)
    tags = NanaTag.objects.all()
    return render(request, 'index.html', {'tasks':tasks, 'tags':tags})

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/register.html', { 'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'registration/register.html', {'form': form})


@login_required
def create_task(request):
    # tasks = NanaTask.objects.filter(owner = request.user)
    context = {}
    form  = NanaTaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.save(commit = False)
            data.owner = request.user
            data.save()
            return redirect('index')

    context['form'] =  form
    return render(request, 'todo/createTodo.html', context)

@login_required
def create_tag(request):
    # tasks = NanaTask.objects.filter(owner = request.user)
    context = {}
    form  = NanaTagForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.save(commit = False)
            data.owner = request.user
            data.save()
            return redirect('index')

    context['form'] =  form
    return render(request, 'todo/createTag.html', context)


@login_required
def mark_as_done(request,id):
    task = NanaTask.objects.get(pk = id)
    task.status = 'Done'
    task.save()
    return redirect('index')