# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    #return HttpResponseRedirect('/static/upload/' + basename)
    response = HttpResponse("Text only, please,from django.", content_type="text/plain")
    return response

