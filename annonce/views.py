from django.shortcuts import render , redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contact, Ad , Category

# Create your views here.
def index(request):
    annonces = Ad.objects.all()
    datas = {
        'annonces': annonces
    }
    return render(request,'index.html',datas)

def annonce(request):
    user = request.user
    annonces = Ad.objects.filter(autor = user)
    datas = {
        'annonces': annonces
    }
    return render(request,'annonce.html',datas)

def add(request):
    user = request.user
    if request.method == 'POST':
        titre = request.POST.get("titre")
        image = request.POST.get("image")
        description = request.POST.get("description")
        category = request.POST.get("category")
        categoty_final = Category.objects.get(name = category)
        ad = Ad()
        ad.title = titre
        ad.image = image
        ad.description = description
        ad.category = categoty_final
        ad.autor = user 
        ad.save()
        return redirect('annonce')
    return render(request,'addannonce.html')

def about(request):
    return render(request,'about.html')
        
def blog(request):
    return render(request,'blog.html')
        
def contact(request):
    if request.method == 'POST':
        username = request.POST.get("name")
        email = request.POST.get("email")
        Subject = request.POST.get("Subject")
        message = request.POST.get("message")
        
        contact = Contact()
        contact.user = username
        contact.email = email
        contact.sujet = Subject
        contact.messages = message
        contact.save()
        return redirect('index')

    return render(request,'contact.html')   
    
def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpwd = request.POST['comfirmpwd']
        if User.objects.filter(username=username):
            messages.error(request, 'username already taken please try another.')
            return redirect('sign_up')
        if User.objects.filter(email=email):
            messages.error(request, 'This email has an account.')
            return redirect('sign_up')
        if not username.isalnum():
            User.error(request, 'username must be alphanumeric')
            return redirect('sign_up')
        if password != confirmpwd:
            User.error(request, 'The password did not match! ')  
            return redirect('sign_up')
        
        my_user = User.objects.create_user(username, email, password)
        my_user.first_name =firstname
        my_user.last_name = lastname
        my_user.is_active = True
        my_user.save()
        
        user = authenticate(username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)
            #### redirection si les infos sont correctes
            return redirect('index')
    return render(request,'sign_up.html')

def connexion(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        user= authenticate(username=name, password=password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect('index')
        else:
            return redirect('connexion')
    return render(request,'login.html')

def cos_logout(request):
    logout(request)
    return redirect('index')