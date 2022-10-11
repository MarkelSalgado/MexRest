from django.shortcuts import render
from .models import Platerak

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


def index(request):
    platerak = Platerak.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'platerak': platerak,
    }
    return HttpResponse(template.render(context, request))


def menu(request):
    platerak = Platerak.objects.all()
    return render(request, 'our_menu.html', {'platerak': platerak})


def add_platera(request):
    platerak = Platerak.objects.all()
    return render(request, 'create_platerak.html', {'platerak': platerak})


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['plt_izena']
    y = request.POST['plt_deskripzioa']
    z = request.POST['plt_osagaiak']
    i = request.POST['plt_prezioa']
    plater = Platerak(izena=x, deskripzioa=y, osagaia=z, prezioa=i)
    plater.save()
    return HttpResponseRedirect(reverse('add_platera'))


def delete(request, id):
    plater = Platerak.objects.get(id=id)
    plater.delete()
    return HttpResponseRedirect(reverse('menu'))


def update(request, id):
    plater = Platerak.objects.get(id=id)
    template = loader.get_template('update_platerak.html')
    context = {
        'plater': plater,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request):
    pre = request.POST['prezio']
    ida = request.POST['ida']
    plater = Platerak.objects.get(id=ida)
    plater.prezioa = pre
    plater.save()
    return HttpResponseRedirect(reverse('menu'))
