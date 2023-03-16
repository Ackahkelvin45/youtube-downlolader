from django.urls import path
from . import views

app_name='main'

urlpatterns=[
    path("",views.indexpage,name='index'),
    path("download/",views.getlink,name='getlink'),
    path("dd/",views.download,name='dd')
]