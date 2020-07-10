"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'ABLity Finance Inc.',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def Blogs(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Blogs.html',
        {
            'title':'Blogs',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def In_the_Media(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/In_the_Media.html',
        {
            'title':'In the Media',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def Lending_Solutions(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Lending_Solutions.html',
        {
            'title':'Lending Solutions',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def Our_Process(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Our_Process.html',
        {
            'title':'Our Process',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def Lender(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Lender.html',
        {
            'title':'Lender',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def Partnerships(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Partnerships.html',
        {
            'title':'Partnerships',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def Business_Finance(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Business_Finance.html',
        {
            'title':'Business_Finance',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def Companyinfo(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Companyinfo.html',
        {
            'title':'Company information',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def BusinessOwner(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/BusinessOwner.html',
        {
            'title':'BusinessOwner',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def Bankinfo(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Bankinfo.html',
        {
            'title':'Bankinfo',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def AssetInfo(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/AssetInfo.html',
        {
            'title':'AssetInfo',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )