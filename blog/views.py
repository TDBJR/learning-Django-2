#===============================================================================
# from django.shortcuts import HttpResponse
# from django.template import loader
#===============================================================================
from django.shortcuts import render


def index(request):
    context={}
    template="blog/index.html"
    return render(request, template, context)




#===============================================================================
# def index(request): #always pass in request in Django views
#     template= loader.get_template('blog/index.html')  # Define the template location in quotes
#     context={}  
#     return HttpResponse(template.render(context, request))
#===============================================================================