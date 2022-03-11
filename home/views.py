from django.shortcuts import render
from .models import  ProjectDetails
# Create your views here.

def coalIndia(request):
    coal = ProjectDetails.objects.all()
    context = {'coal':coal}
    # context = {'wells': wells, 'mylist':mylist}
    return render(request, 'home/viewVatikas.html', context )
