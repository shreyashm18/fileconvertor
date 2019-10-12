from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):
    return render(request,'home.html')

def w2p(request):

    if request.method=='POST':
        wfile=request.FILES['wordfile']
        
        fs=FileSystemStorage()
        fs.save(wfile.name,wfile)
        print(wfile.name)
        print(wfile.size)
        print(wfile.content_type)
        #return redirect('/')
        
    
    return render(request,'w2p.html')