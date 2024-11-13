from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages,auth


def register(request):
    if request.method == 'POST':
        print("request.POST=",request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email'] # pankajmendla@gmail.com
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
        
            return redirect('login')
        else:
         form = RegistrationForm()
         context = {
         'form': form,
           }
        return render(request, 'accounts/register.html', context)
    else:
         form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})








# coursera


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        print("user=",user)

        if user is not None:
            auth.login(request,user)
            return redirect('register')
        else:
            print("i am here in else part")
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')
