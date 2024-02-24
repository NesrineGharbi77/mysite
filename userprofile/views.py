from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile
# Create your views here.
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')

def myaccount_after_login(request):
    return redirect('myaccount')


def frontpage_after_logout(request):
    return redirect('frontpage')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        print(form)

        if form.is_valid():
            user = form.save()
            login(request, user)

            userprofile = Userprofile.objects.create(user=user)

            return redirect('frontpage')
    else :
        print('hello from else')
        form = UserCreationForm()
    
    return render(request, 'userprofile/signup.html', {
        'form': form
    })