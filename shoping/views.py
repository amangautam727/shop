from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
	return HttpResponse("homepage")


def about(request):
	return HttpResponse("about us")

def contact(request):
	return HttpResponse("Contact us")

