# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from pair_stairs.stairs.models import Programmer

def view_stairs(request):
    programmers = list(Programmer.objects.all())
    return render_to_response('stairs.html', RequestContext(request,
            {'programmers_for_columns': programmers[0:-1],
             'programmers_for_rows': programmers[1:]}))

def create_stairs(request):
    if request.method == 'POST':
        names = request.POST['programmer_names'].split(', ')
        Programmer.objects.all().delete()
        for name in names:
            Programmer(name = name).save()
        return redirect(view_stairs)
    return render_to_response('create_stairs.html', RequestContext(request))
