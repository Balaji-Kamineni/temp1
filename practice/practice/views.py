from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    d={
        "name":"balaji",
        "email":"kamineni.balaji@Mitsogo.com",
        "role":"developer",
        "collegues":["anubhav","prasanthi","reddy","shaik"],
        "manager":"sreejith"
    }
    return render(request,"index.html",d)
    return HttpResponse("Hii Balaji")


def aboutUs(request):
    return HttpResponse("i'm torch bearer")
def helper(request,id):
    d={
        1:moreaboutus(request,id),
        2:lessaboutus(request,id)
    }
    return d[id]
    if id==1:
        return moreaboutus(request,id)
    else:
        return lessaboutus(request,id)
    return HttpResponse(id,"we are torch bearers")

def moreaboutus(request,courseid):
    return HttpResponse("this is more about us")


def lessaboutus(request,courseid):
    return HttpResponse("this is less about us")