from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'Home/home.html')

def index2(request):
	return render(request, 'Home/mission.html')

def index3(request):
    return render(request, 'Home/donations.html')
