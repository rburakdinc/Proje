from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Hayvan

# Create your views here.

def index(request):
    hayvanlar = Hayvan.objects.all()

    context = {
        'hayvanlar': hayvanlar
    }
    return render(request,'hayvanlar/list.html',context)

def detail(request,hayvan_id):
    hayvan = get_object_or_404(Hayvan,pk = hayvan_id)
    context = {
        'hayvan':hayvan
    }
    return render(request,'hayvanlar/detail.html',context)

def search(request):
    return render(request,'hayvanlar/search.html')