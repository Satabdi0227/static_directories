from django.shortcuts import render

# Create your views here.
def static_directory(request):
    return render(request,'static_directory.html')