from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.


def index(request):
    # return HttpResponse("This is Homepage")
    context = {"var2": "The Sneaker Store", "variable": "Test paragraph"}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, number=number,
                          desc=desc, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')
    # return HttpResponse("This is Contact page")
