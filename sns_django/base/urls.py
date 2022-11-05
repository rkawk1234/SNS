from django.urls import path
from . import views

##setup url

urlpatterns = [
    path('',views.index, name='index')
]