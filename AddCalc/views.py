from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def result(request):
    fnum = request.GET.get('fnum')
    snum = request.GET.get('snum')
    operations = request.GET.get('operations')

    if fnum.isdigit() and snum.isdigit():
        a = int(fnum)
        b = int(snum)

        if operations == '+':
            c = a + b
            params = {"c": c, "a": a, "b": b, "operations": operations}

        if operations == '-':
            c = a - b
            params = {"c": c, "a": a, "b": b, "operations": operations}

        if operations == '*':
            c = a * b
            params = {"c": c, "a": a, "b": b, "operations": operations}

        if operations == '/':
            c = a / b
            params = {"c": c, "a": a, "b": b, "operations": operations}

        if operations == '//':
            c = a // b
            params = {"c": c, "a": a, "b": b, "operations": operations}

        if operations == '%':
            c = a % b
            params = {"c": c, "a": a, "b": b, "operations": operations}
    return render(request, 'result.html', params)

def about(request):
    return render(request, 'about.html')

def signupUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account Has Been Created Successfully!")
        return redirect('home')
    else:
        return render(request, '404.html')

def loginUser(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "You are successfully logged in!")
            return redirect('home')
        else:
            messages.error(request, "Please Check Your Credentials!")
            return redirect('home')
    else:
        return render(request, '404.html')
    return redirect('home')

def logoutUser(request):
    logout(request)
    return redirect('home')