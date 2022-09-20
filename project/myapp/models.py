from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Client(models.Model):
    client_name=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by =models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table ='client'



class Project(models.Model):
    project_name =models.CharField(max_length=200)
    client_name = models.ForeignKey( Client, on_delete=models.CASCADE )
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now=True )
    created_by = models.ForeignKey( User, on_delete=models.CASCADE )
    class Meta:
        db_table ='project'