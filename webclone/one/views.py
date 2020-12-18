from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'one/base.html')

def search(request):
    s= request.POST.get('search')
    dictq ={'s': s, }
    return render(request,'one/search.html', dictq )
