from django.shortcuts import render
from .models import Bezeroak
from platerak.models import Platerak
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def bezeroikusi(request):
    return render("Nire Bezeroak web")


def bezeroak_index(request):
    bezeroak = Bezeroak.objects.all().values()
    platerak = Platerak.objects.all().values()
    template = loader.get_template('bezeroak_index.html')
    context = {
        'bezeroak': bezeroak,
        'platerak': platerak,
    }
    return HttpResponse(template.render(context, request))
