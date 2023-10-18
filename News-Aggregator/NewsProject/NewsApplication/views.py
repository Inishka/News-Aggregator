from django.shortcuts import render
import html5lib
import requests
from bs4 import BeautifulSoup
from NewsApplication.models import service
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

# GEtting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs/")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)
    
ht_r = requests.get("https://www.hindustantimes.com/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')

ht_headings = ht_soup.find_all('h3',attrs={'class':'hdg3'})

#ht_headings = ht_headings[0:-13] # removing footers

ht_news = []

for ht in ht_headings:
    ht_news.append(ht.text)
    
# Getting images from times of india
#url = 'https://timesofindia.indiatimes.com/briefs/'
#response = requests.get(url)
#soup = BeautifulSoup(response.content, 'html.parser')
#images = []

#for img in soup.find_all('img'):
 #   images.append(img['src'])

#for news image on newspage
#def home(request):
 #   return render(request,'home.html',{'images': images,})

#for frontpage
def index(request):
    return render(request,'index.html')

#for newspage
def home(request):
    return render(request, 'home.html', {'toi_news':toi_news,'ht_news':ht_news})

#for user info

class USERViewset(viewsets.ModelViewSet):
   queryset = USER.objects.all()
   serializer_class=USERSerializer 

#for new users  
def register(request):
    return render(request, 'Register.html')

#for Contact
def contact(request):
    return render(request, 'contactus.html')

#for about Us page
def aboutUs(request):
    if request.method == "GET":
        output = request.GET.get('output')
    return render(request, 'aboutus.html',{'output':output})

#for servicePage
def services(request):
    servicesData=service.objects.all()
    # if request.method == "GET":
    #    st = request.GET.get('servicename')
     #   if st != None:
      #    servicesData = service.objects.filter(service_tittle__icontains = st)  
    data={
        'servicesData':servicesData ,
    }
    return render (request,'service.html',data)