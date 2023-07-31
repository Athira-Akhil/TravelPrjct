from django.shortcuts import render
from . models import place
from . models import team
# Create your views here.
def temp(request):
    obj1=place.objects.all()
    obj2=team.objects.all()
    return render(request,"index.html",{'result':obj1,'teamdtls':obj2})