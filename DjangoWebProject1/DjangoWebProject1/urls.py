"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views



urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('blogs', views.Blogs, name='Blogs'),
    path('In_the_Media', views.In_the_Media, name='In the Media'),
    path('lender', views.Lender, name='lender'),
    path('lending_solutions', views.Lending_Solutions, name='Lending Solutions'),
    path('Our_Process', views.Our_Process, name='Our Process'),
    path('Partnerships', views.Partnerships, name='Partnerships'),
    path('Business_Finance', views.Business_Finance, name='Business_Finance'),
    path('Company_info', views.Companyinfo, name='Company information'),
    path('BusinessOwner', views.BusinessOwner, name='BusinessOwner'),
    path('Bankinfo', views.Bankinfo, name='Bankinfo'),
    path('AssetInfo', views.AssetInfo, name='AssetInfo'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
