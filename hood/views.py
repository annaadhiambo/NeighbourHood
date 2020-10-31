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