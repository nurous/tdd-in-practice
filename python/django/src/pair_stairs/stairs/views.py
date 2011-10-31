# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def create_stairs(request):
    return render_to_response('create_stairs.html', RequestContext(request))
