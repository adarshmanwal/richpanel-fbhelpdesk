from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import urllib
import json
import requests

# Create your views here.
def login(request):
  return render(request, 'login.html')

@login_required
def helpdesk(request):
  social_user = request.user.social_auth.filter(provider='facebook').first()
  access_token = social_user.extra_data['access_token']

  page_access_token = requests.get("https://graph.facebook.com/"+settings.SOCIAL_PAGE_ID+"?fields=access_token&access_token="+access_token).json()

  posts=requests.get("https://graph.facebook.com/v11.0/"+settings.SOCIAL_PAGE_ID+"/visitor_posts?fields=from,created_time,message,full_picture&access_token="+page_access_token['access_token']).json()

  for post in posts['data']:
    print("Getting comments ===> ", post);
    comments=requests.get("https://graph.facebook.com/v11.0/"+post['id']+"/comments?access_token="+page_access_token['access_token']).json()
    post['comments'] = comments['data']

  # print("==========> posts ", posts)

  return render(request, 'helpdesk.html', {'page_access_token': page_access_token['access_token'],'posts': posts['data']})

@login_required
def home(request):
  return render(request, 'home.html')


def postMessage(request):
  pageAccessToken  = request.POST.get('page-access-token')
  message = request.POST.get('message')
  postId = request.POST.get('post-id')
  url = "https://graph.facebook.com/v11.0/"+postId+"/comments?message="+message+"&access_token="+pageAccessToken
  response = requests.post(url)

  return HttpResponse({})
