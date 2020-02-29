from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth import logout
from django.shortcuts import redirect
from . import templates
from .models import Profile

class ProfileView(generic.ListView):
    model = Profile
    template_name = 'tutor/welcome.html'

    #for future, when we grab data from database, currently not functional
    def get_queryset(self):
        return Profile.objects.all()

    #renders the home landing page
    def welcome(request):
        return render(request, template_name)

#class TutorProfileView(generic.ListView):
    

def index(request):
    return render(request, 'tutor/home.html')

