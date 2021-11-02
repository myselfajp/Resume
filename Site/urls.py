from .views import index
from django.urls import path

app_name="Site"

urlpatterns = [
    path('index',index,name='index'),
    path('',index,name='index')
]