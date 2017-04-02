from django.shortcuts import render

# Create your views here.

def jquery_view(request):
    return render(request,'jquery.html')