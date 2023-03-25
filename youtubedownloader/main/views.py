from django.shortcuts import render,redirect
from pytube import YouTube
import os
from pytube.cli import on_progress
from django.contrib import messages
from django.urls import reverse


# Create your views here.


def indexpage(request):
 link=False
 context={
  "link":link
 }
 return render(request,"main/index.html",context=context)


   
        


def download(request):
 if request.method=='POST':
  try:
    resolution=request.POST['res']
    type=request.POST['mime_type']
    type=type[:-1]
    resolution=resolution[:-1]
    link=request.POST['link']
    yt=YouTube(link,on_progress_callback=on_progress)
    home_directory = os.path.expanduser( '~' )
    yt.streams.filter(res=resolution ,mime_type=type).first().download(home_directory + "/downloads")
    

    
    messages.success(request,'Done')
    return redirect(reverse("main:index"))
  except:
    messages.error(request,'Error')
    return redirect(reverse("main:index"))
   

def getlink(request):
  if request.method=='POST':
    try:
      link=request.POST['link']

      yt=YouTube(link)

      title=(yt.title[:30] + '..') if len(yt.title) > 30 else yt.title

      minutes =  int(yt.length )/ 60
      seconds = int(yt.length) % 60
      duration=str(int(minutes)) +":"+str(int(seconds))
      views=yt.views
      thumbnail=yt.thumbnail_url


      yd=yt.streams.filter(type='video',adaptive=True,)

      context={
      'videos':yd,
      'title':title,
      "duration":duration,
      'views':views,
      'link':True,
      'thumbnail':thumbnail,
      "link":link

      }
      return render(request,"main/index.html",context=context)
    except:
      messages.error(request,'Error')
      return redirect(reverse("main:index"))