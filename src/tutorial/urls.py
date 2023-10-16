"""
URL configuration for tutorial project.

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
from django.contrib import admin
from django.urls import include, path, reverse
from django.http import HttpResponse
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from catalog import views

# def index(request):
#     return HttpResponse("Hello, this is a test. If you can't see this, then you suck!!!")


urlpatterns = [
    path('catalog/', include('catalog.urls')),
    #-----------------------------------------Edits--------------------------------------------------#
    # TODO: add a path for editing a contacts
    path('all_sites/contacts_display/edit/<int:id>/',   views.edit_post_contacts,   name='Edit Contacts'),
    path('all_sites/site_display/edit/<int:id>/',       views.edit_post,            name='Edit Site'),
    path('all_sites/hvac_display/edit/<int:id>/',       views.edit_post_hvac,       name='Edit HVAC'),
    path('all_sites/battery_display/edit/<int:id>/',    views.edit_post_battery,    name='Edit Battery'),
    path('all_sites/relion_display/edit/<int:id>/',     views.edit_post_relion,     name='Edit Relion'),
    path('all_sites/access_display/edit/<int:id>/',     views.edit_post_site_access,     name='Edit Access'),
    #------------------------------------------------------------------------------------------------#
    #------------------------------------------Adds--------------------------------------------------#
    path('add_a_site/',                     views.create_post,      name='Add A Site'),
    path('all_sites/battery_display/add/',  views.add_post_battery, name='Add Battery'),
    path('all_sites/hvac_display/add/',     views.add_post_hvac,    name='Add HVAC'),
    path('all_sites/relion_display/add/',   views.add_post_relion,  name='Add Relion'),
    path('all_sites/contacts_display/add/', views.add_post_contacts, name='Add Contacts'),
    path('all_sites/access_display/add/',   views.add_post_site_access, name='Add Access'),
    #------------------------------------------------------------------------------------------------#
    path('all_sites/site_display/delete/<int:id>/', views.delete_post, name='Delete Site'), 
    path('admin/', admin.site.urls),
    path('all_sites/', views.all_sites, name='All Sites'),
    #path('site_display/', views.show_sites, name='Site Display'),
    path('all_sites/site_display/<int:id>/', views.show_sites, name='Site Display'),
    #path('post/create', views.create_post, name='post-create'), #http://10.80.1.43:8001/post/create
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)