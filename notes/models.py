from django.db import models
from . import fields
# Create your models here.

class Note(models.Model):
    # author = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='author')
    # recipent = models.ForeignKey('profiles.Profile',on_delete=models.SET_NULL, related_name='recipent', null=True, blank = True) # odbiorca
    
    author = models.CharField(max_length=30)
    recipent = models.CharField(max_length=30, blank=True)
    content = models.TextField(max_length=200)
    importance = fields.IntegerRangeField(min_value = 1, max_value=3)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if len(self.content) > 10:
            return self.content[:10] + '...'
        return self.content