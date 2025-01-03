from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import conf
from django.db.models import Q  
from .models import Profile, Child, Message
from .forms import CustomUserCreationForm, ProfileForm, ChildForm, MessageForm
from .utils import searchProfiles

def loginUser(request):
    page = 'login'
    context = {'page': page}
    context = {}
    if request.user.is_authenticated:
        return redirect("profiles")
    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]
        print(username, password)
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request, "Username or Password is incorrect")
        
    return render(request, "users/login_register.html", context)

def logoutUser(request):
    logout(request)
    messages.info(request, "User was logged out")
    return redirect("login")

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User was created successfully")
            login(request, user)
            return redirect("edit-account")
        else:
            messages.error(request, "An error occurred during registration")
    context = {'page': page, 'form': form}
    return render(request, "users/login_register.html", context)

def profiles(request):
    profiles, search_query = searchProfiles(request)

    page = request.GET.get('page')
    results = 30
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    context = { 'profiles': profiles, 'paginator': paginator, 'search_query': search_query }

    return render(request, "users/profiles.html", context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {"profile": profile}
    return render(request, "users/user-profile.html", context)

@login_required(login_url="login")
def userAccount(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, "users/account.html", context)

@login_required(login_url="login")
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("account")
    context = {'form': form}
    return render(request, "users/profile_form.html", context)

@login_required(login_url="login")
def createChild(request):
    profile = request.user.profile
    form = ChildForm()
    if request.method == "POST":
        form = ChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.parent = profile
            child.save()
            return redirect("account")
    context = {'form': form}
    return render(request, "users/child_form.html", context)

@login_required(login_url="login")
def updateChild(request, pk):
    profile = request.user.profile
    child = get_object_or_404(Child, id=pk, parent=profile)
    form = ChildForm(instance=child)
    if request.method == "POST":
        form = ChildForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            return redirect("account")
    context = {'form': form}
    return render(request, "users/child_form.html", context)

@login_required(login_url="login")
def deleteChild(request, pk):
    profile = request.user.profile
    child = get_object_or_404(Child, id=pk, parent=profile)
    if request.method == "POST":
        child.delete()
        return redirect("account")
    context = {'object': child}
    return render(request, "users/delete_child.html", context)

@login_required(login_url="login")
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
    return render(request, "users/inbox.html", context)

@login_required(login_url="login")
def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {'message': message}
    return render(request, "users/message.html", context)

def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    try:
        sender = request.user.profile
    except:
        sender = None
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient
            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request, "Your message was sent successfully")
            return redirect("user-profile", pk=recipient.id)
    context = {'recipient': recipient, 'form': form}
    return render(request, "users/message_form.html", context)