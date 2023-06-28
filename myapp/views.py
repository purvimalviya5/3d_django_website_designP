from django.shortcuts import render

# Create your views here.
def Indexpage(request):
    return render(request,'index.html')