from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    error_message = None
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('sales:home')
        else:
            error_message = 'Ups ... something went wrong'

    context = {
        'form': form,
        'error_message': error_message
    }

    return render(request, 'auth/login.html', context)

def signup_view(request):
    if request.method =='POST':
        username =request.POST['username']  # these names should be same as it is in db
        firstname =request.POST['first_name']
        lastname =request.POST['last_name']
        email =request.POST['email_id']
        password =request.POST['password']

        # when errors shows on user click it touch the light beside it and import it
        from django.contrib.auth.models import User
        x= User.objects.create_user(username=username, first_name=firstname,last_name=lastname,email=email,password=password)
        # above all parameters should match from db
        # now save the x var in db
        x.save()
        #print('User created sucessfully!')
        #return HttpResponseRedirect(reverse, 'http://127.0.0.1:8000/')
        return render(request,'auth/sucess.html')

    else:
        return render(request, 'auth/register.html')
