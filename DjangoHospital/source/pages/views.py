from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homeView(request, *args, **kargs):
    print(args, kargs)
    print(request)
    # return HttpResponse("<h1>HELLO WORLD</h1>")
    return render(request, 'home.html', {})

def contactView(request, *args, **kargs):
    return render(request, 'contact.html', {})
    # return HttpResponse("<h1>Contact Page</h1>")

def aboutView(request, *args, **kargs):
    my_content = {
        'name' : 'Helii',
        'numb' : 2842391,
        'my_list': [53238,45235,32525,656243,52564,'End'],
    }
    return render(request, 'about.html', my_content)
    # return HttpResponse("<h1>About Page</h1>")

