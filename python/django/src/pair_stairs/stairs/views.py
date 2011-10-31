# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext

def view_stairs(request):
    return HttpResponse()

def create_stairs(request):
    if request.method == 'POST':
        return redirect(view_stairs)
    return render_to_response('create_stairs.html', RequestContext(request))
