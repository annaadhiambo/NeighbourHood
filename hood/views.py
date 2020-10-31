from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Neighbourhood, healthservices, Business, Health, Authorities, Profile, notifications, Comment
from .forms import notificationsForm, ProfileForm, BusinessForm, CommentForm
import datetime as datetime
import json
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile = Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')

    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def notification(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    all_notifications = notifications.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'notifications.html', {"notifications":all_notifications})

@login_required(login_url='/accounts/login/')
def health(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    healthservices = Health.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'health.html', {"healthservices":healthservices})

@login_required(login_url='/accounts/login/')
def authorities(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    authorities=Authorities.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'authorities.html', {"authorities":authorities})

@login_required(login_url='/accounts/login/')
def businesses(request):
    current_user = request.user
    profile = Profile.objects.get(username = current_user)
    businesses = Business.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'businesses.html', {"businesses":businesses})

@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    profile = Profile.objects.get(username = current_user)

    return render(request, 'user_profile.html', {"profile":profile})

@login_required(login_url='/accounts/login/')
def user_profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(username = user)

    return render(request, 'user_profile.html', {"profile":profile})

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user=request.user
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {"form":form})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == "POST":
        instance = Profile.objects.get(username = current_user)
        form = ProfileForm(request.POST, request.FILES, instance = instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()

        return redirect('Index')

    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request, 'update_profile.html', {"form":form})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)

    if request.method == "POST":
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = current_user
            business.neighbourhood = profile.neighbourhood
            business.save()

        return HttpResponseRedirect('/businesses')

    else:
        form = BusinessForm()

    return render(request, 'business_form.html', {"form":form})