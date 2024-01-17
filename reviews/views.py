# from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
# from django.http import HttpResponse


# def index(request):
#  return HttpResponse("Hello, world!")


# def index(request):
#  name = request.GET.get("name") or "world"
#  return HttpResponse("Hello, {}!".format(name))

from django.shortcuts import render

def index(request):
 # return render(request, "base.html")
 name = "world"
 return render(request, "base.html", {"name": name})
 # return render(request, "base.html", {"name": invalid_name})

def index(request):
 # return render(request, "base.html")
 hint = "Welcome to Bookr"
 return render(request, "base.html", {"hint": hint})

def search(request):
 search = request.GET.get("search")
 return render(request, "bt2.html", {'search': search})



