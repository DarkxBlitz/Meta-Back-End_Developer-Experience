from django.urls import path
from . import views

#To create a route and map a url to a view, you need to create a list sequence using the variable, urlpatterns
#path function can accept 2 arguement, 1st is the route that has a url pattern, 2nd is the relative path and the name of the view function
urlpatterns = [
    path('', views.home),
    path("home/", views.form_view),
    path('menu2/', views.menu2),
]