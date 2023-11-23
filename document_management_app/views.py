from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .models import Document
from .forms import DocumentForm
from django.utils import timezone

def home(request):
    return render(request, 'pages/home.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:       
                login(request, user)         
                return redirect('index')
        else:
            msg = 'Error Login Failed'
            form = AuthenticationForm(request.POST)
            return render(request, 'pages/login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'pages/login.html',{'form': form})    

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')  # Cambia la redirección a la vista 'index'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                return redirect('index')  # Cambia la redirección a la vista 'index'
        else:
            return render(request, 'pages/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'pages/signup.html', {'form': form})
  

def signout(request):
    logout(request)
    return redirect('login_view')

def index(request):
    return render(request, 'pages/index.html')

def consultar(request):
    consulta = Document.objects.all()
    return render(request, 'pages/consultar.html',{'consulta':consulta})
@login_required
def save(request):  
    if request.method == 'POST':
        formulario = DocumentForm(request.POST, request.FILES)
        if formulario.is_valid():            
            documento = formulario.save(commit=False)
            documento.auth_user_id = request.user.id 
            documento.save()
            return redirect('save')
    else:       
        formulario = DocumentForm()

    return render(request, 'pages/save.html', {'formulario': formulario})

