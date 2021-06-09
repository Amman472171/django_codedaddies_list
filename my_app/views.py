from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models

# Create your views here.

BASE_DARAZ_URL='https://www.daraz.com.bd/catalog/?q={}'


def home(request):

    return render(request, 'base.html')

def new_search(request):
    
    search = request.POST.get('search')
    models.Search.objects.create( search=search )

    #print(quote_plus(search))
    final_url = BASE_DARAZ_URL.format(quote_plus(search))
    print(final_url)
    response = requests.get(final_url)
    data =response.text
    soup = BeautifulSoup(data, features = 'html.parser')
    post_titles= soup.find('a').get('title')
    print(post_titles)
    #print(data)
    stuff_for_fontend={
        'search':search,
    }

    return render(request, 'my_app/new_search.html',stuff_for_fontend)
