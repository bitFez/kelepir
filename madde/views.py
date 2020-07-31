from django.shortcuts import render, get_object_or_404, redirect
from .models import Maddeler
from django.views import generic
# Create your views here.
def index(request):
    kelepirler = Maddeler.objects

    context = {'kelepirler':kelepirler}
    return render(request, 'madde/index.html', context)

def voting():
    pass

class MaddeDetailView(generic.DetailView):
    model = Maddeler
