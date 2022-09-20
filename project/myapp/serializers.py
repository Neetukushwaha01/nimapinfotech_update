
from rest_framework import serializers
from .models import Client,Project
from django.contrib.auth.models import User


class RegiserClientSerializer(serializers.ModelSerializer):
    class Meta:
        model =Client
        fields ='__all__'



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields =['username','password','email']



class ClientSerializer(serializers.ModelSerializer):
    created_by =serializers.StringRelatedField()
    class Meta:
        model =Client
        fields ='__all__'


class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model =Project
        fields ='__all__'




class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()

    class Meta:
        model =Project
        fields =['id','project_name','created_at','created_by']