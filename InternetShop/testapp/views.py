from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        count = request.POST.get("count")
        cost = request.POST.get("cost")
        return HttpResponse("<h2>Name {0}</h2>".format(name)+"<h2>Count {0}</h2>".format(count)+"<h2>Cost {0}</h2>".format(cost))
    else:
        userform = UserForm()
        return render(request, "testapp/index.html", {"form": userform})

