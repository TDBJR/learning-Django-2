from django.conf.urls import  url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='joins'),
    
    
    

        
    #This url needs to be last in the list of urls
    # I think ref_id is just a variable that captures a raw data input as it's value so what ever object you send it seems to capture and become it
    url(r'^(?P<ref_id>.*)$',views.share, name='share'),
    #url(r'^(?P<ref_id>[\w.@+-]+)/$',views.share, name='share'),

    
]





