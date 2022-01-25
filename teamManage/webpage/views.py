from django.shortcuts import render, HttpResponse

# CHANGE TO CLASS BASED VIEW??
def home(request):
	return HttpResponse("List of Team Members")

