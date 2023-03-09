"""juanthosa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

#from django.conf.urls import include, url
"""
from django.urls import include, re_path
from django.contrib import admin
from showstatic import views
from polls import views
"""

from django.contrib import admin
from django.urls import path
from showstatic import views
urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.EmailAttachementView.as_view(), name='emailattachment'),
   #path('',views.home,name='index'),
   path('about/',views.about,name='about'),
   path('transporte-fluvial/',views.transportefluv,name='transporte-fluvial'),
   path('transporte-terrestre/',views.transporteterr,name='transporte-terrestre'),
   path('transporte-aereo/',views.transporteaer,name='transporte-aereo'),
   path('download/<str:filename>/', views.download_pdf_file, name='download_pdf_file'),
   path('contacto/', views.contact.as_view(), name='contact'),
   path('pqrs/', views.contact.as_view(), name='contact'),
   path('mision/', views.mision, name='mision'),
   path('vision/', views.vision, name='vision'),
   path('login/', views.login, name='login')
]

"""
urlpatterns = [
    re_path(r'^$', views.home, name='index'),
    re_path(r'^admin/', admin.site.urls),
]
"""


