from django.urls import path
from . import views

##setup url

urlpatterns = [
    path('',views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('settings',views.settings, name='settings'),
    path('upload',views.upload,name='upload'),
    path('like-post', views.like_post, name='likst-post'),
    path('profile/<str:pk>',views.profile, name='profile'),
    path('follow',views.follow, name='follow'),
    path('search',views.search, name='search'),

]