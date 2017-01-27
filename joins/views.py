from django.shortcuts import render, HttpResponseRedirect, Http404
from .models import Join
from .forms import  JoinForm


# A method to obtain the ip of users who fill out a form
def get_ip(request):
    try:
        x_forward = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    
    except:
        ip=''
    return ip


import uuid # uuid seems to be a random number-letter string generator
def get_ref_id():
# Just creating a random 10 digit number-letter string to use as a user id
    ref_id = str(uuid.uuid4())[:11].replace('-','').lower()# Replaces - with nothing, basically deletes - from the data
    try:
# If a existing ref_id is found that matches the randomly generated one we regenerate a new one
        check_for_existing_id = Join.objects.get(ref_id=ref_id)# Call the object by the generated ref_id if it fails except runs, if it succeeds in finding an object rerun the generation
        get_ref_id()                                     #object.ref_id = variable ref_id
    
    except:
        return ref_id
    
# ref_id is passed in by the url.
# With this try we are stating that it should find a created object with that ref_id or raise a 404
def share(request, ref_id):
    try:
        join_obj = Join.objects.get(ref_id = ref_id)       # becomes The actual join object 
#Finding the friends that share the same ForeignKey
        friends_referred = Join.objects.filter(friend=join_obj) #friend is a attribute ForeignKey we gave to the Join class
        #friends = friends_referred.count()
# Counting the amount of friends you have referred
        count = join_obj.referral.all().count()
        ref_url = "127.0.0.1:8000/joins/?ref=%s"%(join_obj.ref_id)
# Passing in the ref_id of the object
        context={'ref_id': join_obj.ref_id, 'count':count, 'ref_url':ref_url,}# 'friends':friends}
        template = "joins/share.html"
        return render(request, template, context)
    except:
        raise Http404
     
def index(request):
    try:
#if you visit the index with the url containg a objects ref_id. We then set  'join_id'= The object.id of the object that used that ref_id  using middleware
        join_id = request.session['join_id_ref'] # Sets the ID captured by middleware to be set to a variable if there was a ?ref=
# This is serching for a Join object that has that id
        obj = Join.objects.get(id=join_id)       
    except:
        obj = None
    print("This user was referred by",obj)  
    form = JoinForm(request.POST or None) #requesting any POST action taken from this page
    if form.is_valid():
# commit false allows you to step in before the object is created and alter its attributes
        new_join = form.save(commit=False) # Becoming the data but not submiting it
        email = form.cleaned_data['email']
# making a new variable to have the data saved to and a second to hold the True or False value
        new_join_old, created1 = Join.objects.get_or_create(email=email)
# get_or_create passes 2 variables the first contains the data the second contains True or False depending 
# on if an object was created. both can be named anything
        if created1:
            new_join_old.ref_id = get_ref_id()
            if not obj == None: # If the obj returned a Join.objects.get(id=join_id) and became that object append that objects ForeignKey to this object
                new_join_old.friend = obj
            new_join_old.ip_address = get_ip(request)
            new_join_old.save()
# printing out the objects that share a ForeignKey           
            #===================================================================
            # print(Join.objects.filter(friend=obj).count())
            # print(Join.objects.filter(friend=obj))
            # print(obj.referral.all())
            #===================================================================
            
# This is redirecting the page to a url/ that contains the attribute  ref_id of the created object       
        return HttpResponseRedirect('%s' %(new_join_old.ref_id))
        #   may or may not need to be '/%s' depending on address 
      
# This is redirecting if the form was not filled out properly 
    context = {'form':form}
    template = "joins/index.html"
    return render(request, template, context)




















