from joins.models import Join


#When Middleware is installed it is run automatically when interacting with a webapp
class ReferMiddleware():
    def process_request(self,request):
# request.GET.get(' ')  will search the address bar for a variable that has ?before it and = after  ?ref= in this case. It will store the variable and its = contents
# You can chain them in the address bar with ?ref=123&dog=abc in this case both ref and dog can be stored
            ref_id = request.GET.get('ref')                    
            try:
# Using the ref_ id to set a variable to that object with the ref_id
                obj = Join.objects.get(ref_id = ref_id)                          
            except:
                obj = None
# Clearing the session so it is not reused on further sign-ups
                if 'join_id_ref' in request.session: 
                    del request.session['join_id_ref']
            if obj:
                ref_id=None
#Because sessions are Serialized in Json you can only set an objects.id an not its entire contents
                request.session['join_id_ref'] = obj.id                
            else:
                print('There was no ?ref= captured')   
 
 
 
 
 
 
 
 
    








