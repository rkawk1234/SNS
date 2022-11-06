from django.urls import path
from . import views

##setup url

urlpatterns = [
    path('',views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    # path('profile',views.profile, name='profile')

]