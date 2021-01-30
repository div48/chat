from django.contrib.auth import login, authenticate
from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from chat.settings import EMAIL_HOST_USER
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import Profile, Image
from django.core.mail import send_mail
from twilio.rest import Client
from django.contrib.auth.hashers import make_password
import math, random
from django.contrib.auth.decorators import login_required

from django.contrib.sites import requests
from django.shortcuts import render
import json
import requests
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('log')


def index(request):
    return render(request, 'Front/landing.html')

def log(request):
    return render(request, 'Front/login.html')

def sign(request):
    return render(request, 'Front/signup.html')

@login_required(login_url='log')
def home(request):
    all_images = Image.objects.all()
    comm=Comment.objects.all()
    user=Profile.objects.all()
    send_url = "http://api.ipstack.com/check?access_key=9bf71367e3105cd39e12c27c47f93749"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    city = geo_json['city']


    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&cnt=3&appid=98e6745c3682b89eacc6c65fe2409f6e'
    city = 'Jalandhar'
    print(city)
    city_weather = requests.get(url.format(city)).json()

    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon'],
        "pressure": city_weather['main']['pressure'],
        "humidity": city_weather['main']['humidity'],
        'wind': city_weather['wind']['speed'],
        'cloud': city_weather['clouds']['all']
    }
    import weathercom

    weatherDetails2 = weathercom.getCityWeatherDetails(city=city, queryType="ten-days-data")
    y = json.loads(weatherDetails2)
    weather2 = {
        'city': city,
        'date': y['vt1dailyForecast']['validDate'],
        'day': y['vt1dailyForecast']['dayOfWeek'],
        'temp': y['vt1dailyForecast']['day']['temperature'],
        'description': y['vt1dailyForecast']['day']['phrase'],
        "pre": y['vt1dailyForecast']['day']['precipPct'],
        "humidity": y['vt1dailyForecast']['day']['humidityPct'],
        'wind': y['vt1dailyForecast']['day']['windSpeed'],
    }
    import datetime

    x = datetime.datetime.now()

    date={
        'day':x.strftime("%d"),
        'month': x.strftime("%B"),
        'year': x.strftime("%Y"),
        'week': x.strftime("%A"),
        'time': x.strftime("%X"),

    }

    context = {
        'products':all_images,
        'user':user,
        'comments':comm,
        'weather': weather,
        'weather2': weather2,
        'date':date,
        # 'wea':x
    }
    return render(request, "display/home.html",context )

@login_required(login_url='log')
def weather(request):
    send_url = "http://api.ipstack.com/check?access_key=your api key"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    city = geo_json['city']
    print(city)

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&cnt=3&appid=your api key'
    city = 'Jalandhar'
    city_weather = requests.get(url.format(city)).json()

    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon'],
        "pressure": city_weather['main']['pressure'],
        "humidity": city_weather['main']['humidity'],
        'wind': city_weather['wind']['speed'],
        'cloud': city_weather['clouds']['all']
    }
    import weathercom

    weatherDetails2 = weathercom.getCityWeatherDetails(city=city, queryType="ten-days-data")
    y = json.loads(weatherDetails2)
    weather2 = {
        'city': city,
        'date': y['vt1dailyForecast']['validDate'],
        'day': y['vt1dailyForecast']['dayOfWeek'],
        'temp': y['vt1dailyForecast']['day']['temperature'],
        'description': y['vt1dailyForecast']['day']['phrase'],
        "pre": y['vt1dailyForecast']['day']['precipPct'],
        "humidity": y['vt1dailyForecast']['day']['humidityPct'],
        'wind': y['vt1dailyForecast']['day']['windSpeed'],
    }
    print(weather2)

    context = {
        'weather': weather,
        'weather2': weather2,
        'range': range(7),
        # 'wea':x
    }
    return render(request,'display/weather.html', context)

def login_view(request):
    if request.method == 'POST':

        # form = LoginForm(request.POST)
        if request.POST.get('your_name') and request.POST.get('your_pass'):

            username = request.POST['your_name']
            password = request.POST['your_pass']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if(Profile.objects.filter(user=username,email_confirmed=True,phone_confirmed=True)):
                     return HttpResponseRedirect(reverse('home'))
                else:
                    messages.warning(request, 'Email or Phone is not verified')
                    return HttpResponseRedirect(reverse('log'))
            else:
                messages.warning(request, 'Password  is incorrect ')
                return HttpResponseRedirect(reverse('log'))
        else:
            messages.warning(request, 'Enter a Valid Input')
            return HttpResponseRedirect(reverse('log'))


def otp(request):
    digits = "0123456789"
    OTP = ""

    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def signup(request):
    if request.method == 'POST':
        print("1")
        if request.POST.get('username') and request.POST.get('F_name') and request.POST.get('L_name') and request.POST.get('email') and request.POST.get('mobile') and request.POST.get('pass') and request.POST.get('repass'):
            print("22")
            v1 = (request.POST['F_name'])
            v2 = (request.POST['L_name'])
            v3 = (request.POST['username'])
            v4 = (request.POST['email'])
            v5 = (request.POST['pass'])
            v6 = (request.POST['repass'])
            v8 = (request.POST['mobile'])
            print("2")
            if v5 == v6:
                if len(v5)>=7:
                    password1=make_password(v5)
                    u=User.objects.filter(username=v3)


                    if not u :
                        v = Profile.objects.filter(email=v4)
                        x = Profile.objects.filter(mobile=v8)

                        if not v:
                            if not x:
                                subject = 'Welcome to Farmr. A social media Platform for farmer.' \
                                          'Your Verification Code is :'
                                message = otp(request)
                                recepient = str(v4)
                                send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)

                                to = '+91' + v8
                                client = Client('Token id', 'key')
                                potp = otp(request)
                                client.messages.create(
                                    body='Your verification otp is ' + potp,
                                    to=to, from_='+12059648218')

                                d = Profile.objects.create(user=v3, first_name=v1, last_name=v2, mobile=v8, email=v4)
                                d.save()
                                E = User.objects.create(username=v3, email=v4, password=password1)
                                E.save()

                                context = {
                                    'username': v3,
                                    'eotp': message,
                                    'potp': potp,
                                }
                                return render(request, 'Front/OTP.html', context)





                            else:
                                messages.warning(request, 'Phone is in Use, Try new ')
                                return HttpResponseRedirect(reverse('sign'))
                        else:
                            messages.warning(request, 'Email is in Use, Try new ')
                            return HttpResponseRedirect(reverse('sign'))

                    else:
                        messages.warning(request, 'Username not available , Try new')
                        return HttpResponseRedirect(reverse('sign'))
                else:
                    messages.warning(request, 'Password  is too small ')
                    return HttpResponseRedirect(reverse('sign'))
            else:

                messages.warning(request, 'Password  not match ')
                return HttpResponseRedirect(reverse('sign'))



def add(request, username, eotp, potp):
        v=eotp
        x=potp
        u=username
        context = {
                      'username':u,
                      'eotp':v,
                         'potp': x,
                    }
        if request.method == 'POST':
            if request.POST.get('email_otp') and request.POST.get('phone_otp'):
                v3 = (request.POST['email_otp'])
                v2 = eotp
                v4 = (request.POST['phone_otp'])
                v5 = potp

                if v3 == v2:
                    messages.warning(request, 'Email account is Verified ')
                    s = Profile.objects.get(user=username)
                    print(s)
                    Profile.objects.filter(user=username).update(email_confirmed=True)
                    if v4 == v5:
                        messages.warning(request, 'Mobile number is Verified ')
                        s = Profile.objects.get(user=username)
                        print(s)
                        Profile.objects.filter(user=username).update(phone_confirmed=True)
                        return render(request, 'Front/login.html', )
                    else:
                        messages.warning(request, 'Phone OTP not match ')
                        return render(request, 'Front/OTP.html', context)

                else:
                    messages.warning(request, 'Email OTP not match ')
                    return render(request, 'Front/OTP.html', context)




@login_required(login_url='log')
def upload(request):
    current_user = request.user
    print(current_user)
    # imageuploader = current_user\
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.imageuploader_profile =request.user.username
            post.save()
            return redirect('home')


    else:
        form = PostForm
        return render(request, 'display/fileUpload.html', {"form": form})

@login_required(login_url='log')
def BlogPostLike(request, pk):
    print(request.POST.get('blogpost_id'))
    print("1")
    post = get_object_or_404(Image, id=request.POST.get('blogpost_id'))
    print(post)
    if post.image_likes.filter(id=request.user.id).exists():
        post.image_likes.remove(request.user)
        print(post.likes)
        post.likes =post.likes-1
        post.save()
        print(post.likes)
    else:
        print(request.user)
        post.image_likes.add(request.user)
        post.likes=post.likes+1
        post.save()
        print(post.likes)

    return redirect('home')

@login_required(login_url='log')
def comment(request, pk):
    print(pk)
    post = Image.objects.filter(id=pk)
    print(post[0])

    if request.method == 'POST':
        print("1")
        if request.POST.get('comment') :
            v3 = (request.POST['comment'])
            print(v3)
            comment = Comment.objects.create(post=pk,user=request.user,content=v3)
            comment.save()
            return redirect(home)
    return redirect(home)

@login_required(login_url='log')
def profile(request,user):
    print(user)
    useer=Profile.objects.filter(user=user)
    print(useer)
    x=Image.objects.filter(imageuploader_profile=user)
    context = {
        'products': x,
        'user': useer,

    }


    return render(request, "display/profile.html",context )


# crops Section

@login_required(login_url='log')
def jute(request):
    return render(request, 'display/jute-block.html')
@login_required(login_url='log')
def rice(request):
    return render(request, 'display/rice-block.html')
@login_required(login_url='log')
def pulses(request):
    return render(request, 'display/pulses-block.html')
@login_required(login_url='log')
def sugarcane(request):
    return render(request, 'display/sugarcane-block.html')

@login_required(login_url='log')
def wheat(request):
    return render(request, 'display/wheat-block.html')
@login_required(login_url='log')
def maize(request):
    return render(request, 'display/maize-block.html')

# notice board
@login_required(login_url='log')
def pmk(request):
    return  HttpResponseRedirect('https://www.pmkisan.gov.in')
@login_required(login_url='log')
def pmm(request):
    return redirect('https://www.pmkmy.gov.in')
@login_required(login_url='log')
def pmb(request):
    return redirect('https://www.pmfby.gov.in/')
@login_required(login_url='log')
def pms(request):
    return redirect('https://www.soilhealth.dac.gov.in/')
