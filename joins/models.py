from django.db import models





class Join(models.Model):    
    friend = models.ForeignKey('self', related_name='referral', null=True, blank=True)
# This is creating a variable to store an id we will generate with a method at a later time                                   
    ref_id = models.CharField(max_length=120, default="abc",unique=True)
# ip_adress is a variable that can be named anything. defualt is needed as a placeholder ( i think for pre-existing Join objects)
    ip_address = models.CharField(max_length=120, default='abc')
    email = models.EmailField() # means there can only be one email per entry (No duplicates)
    timestamp = models.DateTimeField(auto_now_add = True,  auto_now=False)
    # auto_now_add timestamps the object when it is created but auto_now timestamps on every update of the object
    updated = models.DateTimeField(auto_now_add = False,  auto_now=True)
    
    
    def __str__(self):
        return self.email
    
    class Meta:
# This is setting it so that there can be no duplicate Join objects with the same email and ref_id
        unique_together = ('email', 'ref_id',) # set in a tuple
# unique_together is a built-in  
    
#===============================================================================
# class JoinFriends(models.Model):
# # This is a ForeignKey that only allows one link, so Join can have only one JoinFriends linked to it
#     email = models.OneToOneField(Join, related_name='Sharer')
# # ManyToManyField is a ForeignKey for JoinFriends it lets an unlimited amount of Join objects be joined to JoinFriends
#     friends = models.ManyToManyField(Join, related_name='Friend', null=True, blank=True)
# # ForeignKey is like ManyToMany but it belongs to the parent object
#     emailall = models.ForeignKey(Join, related_name='emailall')
#     
#     def __str__(self):
#         return self.email.email
#===============================================================================

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    