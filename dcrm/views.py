from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import Records

# Create your views here.

def home(request):
    #DO SOMETHING

    records = Records.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "Error! Try again")  
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})




def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Welcome! Enjoy staying here.")
            return redirect('home')
    else:
        form = SignUpForm
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})


    return render(request, 'register.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")  
    return redirect('home')


def add_record(request):
    forms = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            add_record = forms.save()
            messages.success(request, "Record Added Successfully!")
            return redirect('home')
        return render(request, "add_record.html", {'forms':forms})
    else:
        messages.success(request, "Log-in first.")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Records.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
           form.save()
           messages.success(request, "Record has been successfully updated!")
           return redirect('home')
        return render(request, "update_record.html", {'form':form})
    else:
        messages.success(request, "Log-in first.")
        return redirect('home') 



def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Records.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record has been successfully deleted.")
        return redirect('home')

    else:
        messages.success(request, "Log-in first.")
        return redirect('home') 


