"""
URL configuration for chefsTable project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''#OR instead of above, add:
 from django.urls import path, include

and inside the urlpattern variable add:
path('', include('myfirstapp.urls'))
'''

#path(sub_directoryname, where_the_url_is_in_the_code)
from django.contrib import admin
from django.urls import path
from myfirstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', views.hello, name = "hello"),
    path('homepage', views.homepage, name = "homepage"),
    path('menu', views.menu, name = "menu"),
    path("home/", views.form_view, name = "form"),
    path('menu2', views.menu2, name="menu2"),
]
