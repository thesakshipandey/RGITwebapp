from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'depts/index.html')

def comp(request):
    return render(request, 'depts/comp.html')

def IT(request):
    return render(request, 'depts/IT.html')

def EXTC(request):
    return render(request, 'depts/EXTC.html')

def FE(request):
    return render(request, 'depts/FE.html')

def mech(request):
    return render(request, 'depts/mech.html')

def instru(request):
    return render(request, 'depts/instru.html')

def about(request):
    return render(request, 'depts/about.html')

def dept(request):
    return render(request, 'depts/dept.html')

def compstaff(request):
    return render(request, 'depts/staff.html')
