from django.shortcuts import render

def Index(request) :
    return render(request, 'myapp/index.html')

def About_page(request) :
    return render(request, 'myapp/About.html')

def Contact_page(request) :
    return render(request, 'myapp/Contact.html')