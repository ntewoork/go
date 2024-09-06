from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def Index(a):
        context = {
            'fea':feature.objects.all(),
            'te':text.objects.all(),
            'our':our.objects.all(),
            'ser':sevice.objects.all(),
            'work':work.objects.all(),
            'plan':plan.objects.all(),
            'team2':team2.objects.all(),
            'team':team.objects.all(),
            'ans':answer.objects.all(),
            'by':by.objects.all()
        }
        return render(a, 'index.html', context)


def Send(a):
    if a.method == "POST":
        ism = a.POST['ism']
        e_mail = a.POST['e_mail']
        tel = a.POST['tel']
        pro= a.POST['pro']
        questions.objects.create(ism=ism, e_mail=e_mail, tel=tel, pro=pro)
        messages.success(a, 'habar junatildi')
        return redirect('/')
   
def Register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
               form.save(form)
            #    user = form.cleaned_data.get('username')
               messages.success(request, 'info')
               return redirect('/login/')
    else:
        form = UserCreationForm
    
    context = {
        'form':form
    }
    return render(request, 'registration/register.html', context)
    

def Login(request):
     if request.method == "POST":
        username = request.POST.get[username]
        password = request.POST.get[password]
        form =authenticate(username=username, password=password)
        if form is not None:
             login(request, form)
             user = form.cleaned_data.get('username')
             messages.success(request, 'info')
             return redirect('/login/')
        return render(request, 'regitration/login.html')
     
def Logout(request):
     logout(request)
     messages.success(request, 'info')
     return redirect('/')
            
        

