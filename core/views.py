# -*- coding: utf8 -*-

# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context
#from django.template.defaulttags import load
#from django.template.loaders.app_directories import Loader
#from django.core.context_processors import request
from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request):
    from django.conf import settings
    context = {'STATIC_URL' : settings.STATIC_URL}
    return render_to_response('index.html', context)
    t = loader.get_template('index.html')
    c = Context()
    
    content = t.render(c)
    
    return HttpResponse(content)
