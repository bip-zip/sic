from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=255,null=False, blank=False)
    contact = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null= False, blank=False)
    created = models.DateTimeField(auto_now=True)

    





