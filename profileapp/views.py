from django import forms
from django.shortcuts import render, redirect
import json

from django.http import HttpResponse

from .forms import CreateUserForm, ProfileForm
from .decorators import unauthenticated_user

from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta
from .models import Profile, Seizures, Alert
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from calendar import monthrange
from urllib.parse import unquote

# Create your views here.

@login_required(login_url='login')
def index(request):
    now = timezone.now()
    user = request.user
    # Calculate the start and end dates for the weekly, hourly, and monthly intervals
    start_of_week = now - timedelta(days=6)
    end_of_week = now
    start_of_hour = now - timedelta(hours=1)
    end_of_hour = now
    start_of_month = now - timedelta(days=30)
    end_of_month = now
    start_of_day = now - timedelta(hours=24)
    end_of_day = now
    weekly_incidents = Seizures.objects.filter(user=user,timestamp__range=[start_of_week, end_of_week]).count()
    hourly_incidents = Seizures.objects.filter(user=user,timestamp__range=[start_of_hour, end_of_hour]).count()
    monthly_incidents = Seizures.objects.filter(user=user,timestamp__range=[start_of_month, end_of_month]).count()
    incidents = Seizures.objects.filter(user=user, timestamp__range=[start_of_day, end_of_day]).count()
    last_incident = Seizures.objects.filter(user=user).order_by('-timestamp').first()
    last_location = last_incident.location if last_incident else "N/A"
    last_incident_date = last_incident.timestamp if last_incident else "N/A"
    last_seizures = Seizures.objects.filter(user=user).order_by('-timestamp')[:4]
    last_alerts = Alert.objects.filter(user=user).order_by('-timestamp')[:4]
    context = {
        'weekly_incidents': weekly_incidents,
        'hourly_incidents': hourly_incidents,
        'monthly_incidents': monthly_incidents,
        'incidents' : incidents,
        'last_location': last_location,
        'last_incident_date': last_incident_date,
        'last_seizures' : last_seizures,
        'last_alerts' : last_alerts
    }
    print(context)
    return render(request, 'profileapp/home.html',context)

@csrf_exempt
def seizure_detected(request):
    if request.method=='POST' :
        data = json.loads(request.body.decode('utf-8'))
        token = data.get('pushbullet_token')
        loc = data.get('location')
        loc = unquote(str(loc))
        # print(token)
        user = Profile.objects.filter(push_bullet_token=token).first()
        if not user:
            return JsonResponse({'error': 'Invalid Pushbullet token'}, status=401)
        seizure = Seizures(user=user.user,location=str(loc))
        seizure.save()
        alert = Alert(user=user.user,token=token)
        alert.save()
        return JsonResponse({'message': 'Seizure and message record created successfully'})
    return JsonResponse({'message':'Not a post request'})

@login_required(login_url='login')
def profile(request):
    if(request.method == 'POST'):
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        print(form)
        if(form.is_valid()):
            form.save()
            username = request.user.username
            messages.info(request, f'{username}, Profile Updated!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    

    context = {
        'form': form,
    }
    return render(request, 'profileapp/profile.html', context)


def maps(request):
    return render(request, 'profileapp/maps.html')


@unauthenticated_user
def login_user(request):
    form = CreateUserForm()

    if(request.method == 'POST'):
        if('loginform' in request.POST):
            username = request.POST.get('username2')
            password = request.POST.get('password2')

            user = authenticate(request, username=username, password=password)

            if(user is not None):
                login(request, user)
                messages.info(request, f'{username}, Welcome!')
                return redirect("/")
            else:
                messages.info(request, 'Invalid Username/Password')
                return redirect('login')
        elif('signupform' in request.POST):
            form = CreateUserForm(request.POST)
            if(form.is_valid()):
                form.save()
                messages.info(request, 'Account Created')
                return redirect('login')
            else:
                context = {'form':form}
                return render(request, 'profileapp/signup.html', context)


    context = {'form':form}
    return render(request, 'profileapp/login.html', context)

@unauthenticated_user
def register_user(request):
    form = CreateUserForm()

    if(request.method == 'POST'):
        if('loginform' in request.POST):
            username = request.POST.get('username2')
            password = request.POST.get('password2')

            user = authenticate(request, username=username, password=password)

            if(user is not None):
                login(request, user)
                messages.info(request, f'{username}, Welcome!')
                return redirect("/")
            else:
                messages.info(request, 'Invalid Username/Password')
                return redirect('login')
        elif('signupform' in request.POST):
            form = CreateUserForm(request.POST)
            if(form.is_valid()):
                form.save()
                messages.info(request, 'Account Created')
                return redirect('login')
            else:
                context = {'form':form}
                return render(request, 'profileapp/signup.html', context)


    context = {'form':form}
    return render(request, 'profileapp/signup.html', context)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')

