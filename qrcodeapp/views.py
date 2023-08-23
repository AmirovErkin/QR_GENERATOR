
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import qrcode
import time
from . import forms
def home(request):
    return HttpResponse("Assalomu alekum dasturimga hush kelibsiz siz urls ga<br>"
                        "<br>/wifi"
                        "<br>/link"
                        "<br>social/twitter"
                        "<br>social/telegram"
                        "<br>social/instagram<br>"
                        "Shu kommandalar orqali dasturimizni ishlatishingiz mumkin")
def wifi_generator(request):

    if request.method == 'POST':
        form = forms.WifiForm(request.POST)
        if form.is_valid():
            wifi_name = form.cleaned_data['wifi_name']
            encryiption = form.cleaned_data['encryiption']
            password = form.cleaned_data['password']
            wifi_info = f"WIFI:S:{wifi_name};T:{encryiption};P:{password};;"
            img = qrcode.make(wifi_info)
            img_name = 'qr' + str(time.time()) + '.png'
            img.save(str(settings.MEDIA_ROOT) + '/' + str(img_name))
            return render(request, 'qrcodeapp/index.html', {'img_name': img_name, 'form': form})
    else:
        form = forms.WifiForm()

    return render(request, 'qrcodeapp/index.html', {'form': form})

def generate_link_code(request):
    if request.method == 'POST':
        form = forms.LinkForm(request.POST, request.FILES)
        if form.is_valid():
            link = form.cleaned_data['link']
            link_inf = qrcode.make(link)
            img_name = 'qr' + str(time.time()) + '.png'
            link_inf.save(str(settings.MEDIA_ROOT) + '/' + str(img_name))
            form.save()
            return render(request, 'qrcodeapp/link.html', {'form': form, 'img_name':img_name})
    else:
        form = forms.LinkForm()
    return render(request, 'qrcodeapp/link.html', {'form': form})

def social_insta(request):
    if request.method == 'POST':
        form = forms.SocialForm(request.POST, request)
        if form.is_valid():
            username = form.cleaned_data['username']
            url = f"https://instagram.com/{username}"
            social_inf = qrcode.make(url)
            img_name = 'qr' + str(time.time()) + '.png'
            social_inf.save(str(settings.MEDIA_ROOT) + '/' + str(img_name))
            form.save()
            return render(request, 'qrcodeapp/social.html', {'form': form, 'img_name': img_name})
    else:
        form = forms.SocialForm()
    return render(request, 'qrcodeapp/social.html', {'form': form})

def social_twitter(request):
    if request.method == 'POST':
        form = forms.SocialForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            url = f"https://twitter.com/{username}"
            social_inf = qrcode.make(url)
            img_name = 'qr' + str(time.time()) + '.png'
            social_inf.save(str(settings.MEDIA_ROOT) + '/' + str(img_name))
            form.save()
            return render(request, 'qrcodeapp/social.html', {'form': form, 'img_name': img_name})
    else:
        form = forms.SocialForm()
    return render(request, 'qrcodeapp/social.html', {'form': form})

def social_telegram(request):
    if request.method == 'POST':
        form = forms.SocialForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            url = f"https://t.me/{username}"
            social_inf = qrcode.make(url)
            img_name = 'qr' + str(time.time()) + '.png'
            social_inf.save(str(settings.MEDIA_ROOT) + '/' + str(img_name))
            form.save()
            return render(request, 'qrcodeapp/social.html', {'form': form, 'img_name': img_name})
    else:
        form = forms.SocialForm()
    return render(request, 'qrcodeapp/social.html', {'form': form})