from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from loginapp import views

urlpatterns = [
    #path('favicon.ico',RedirectView.as_view(url='/static/images/favicon.ico')),
    path('',views.index,name="loginapp"),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logoutUser")
]