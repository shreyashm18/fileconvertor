from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def w2p(request):
    return render(request,'w2p.html')