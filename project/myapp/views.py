from django.contrib.auth import authenticate,login
from django.shortcuts import render

# Create your views here.

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegiserClientSerializer,ClientSerializer,ProjectSerializer,CreateProjectSerializer,LoginSerializer
from .models import Client,Project

from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

class ClientList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk=None):
        print(request.user)
        all_clients =Client.objects.filter()
        clients_list =ClientSerializer(all_clients,many=True)
        return Response( clients_list.data, status=status.HTTP_200_OK )

    def post(self,request=None):
        result={}
        if not request.data.get('client_name'):
            result['error']="client_name required."
            return Response( result, status=status.HTTP_201_CREATED )
        if not request.data.get('created_by'):
            result['error']="created_by required."
            return Response( result, status=status.HTTP_400_BAD_REQUEST )

        serializer =RegiserClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            client_name =request.data.get( 'client_name' )
            message =f"{client_name} Register Successfully"
            return Response( message, status=status.HTTP_200_OK )
        else:
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )



#all  details put and delect funstion code start>
class ClientDetails(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self,pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        client =self.get_object(pk)
        client_list =ClientSerializer(client)
        return Response(client_list.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        print(request)
        client = self.get_object( pk )
        print(request.data)
        serilizer =RegiserClientSerializer(client, data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response( serilizer.data, status=status.HTTP_202_ACCEPTED )
        else:
            return Response( serilizer.errors, status=status.HTTP_400_BAD_REQUEST )

    def delete(self,request,pk):
        client = self.get_object( pk )
        client.delete()
        return Response({'message':"Client Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
# all  details put and delect funstion code close>

# <project show and add list start code>
class ProjectList( APIView ):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        all_project = Project.objects.filter(created_by=request.user)
        project_list = ProjectSerializer( all_project, many=True )
        return Response( project_list.data, status=status.HTTP_200_OK )

    def post(self, request=None):
        result = {}
        if not request.data.get( 'project_name' ):
            result['error'] = "project_name required."
            return Response( result, status=status.HTTP_201_CREATED )

        request.data._mutable = True
        request.data['created_by'] = str(request.user.pk)
        print(request.user.pk)
        request.data._mutable = False

        serializer = CreateProjectSerializer( data=request.data )
        if serializer.is_valid():
            serializer.save()
            project_name = request.data.get( 'project_name' )
            message = f"{project_name} Register Successfully"
            return Response( message, status=status.HTTP_200_OK )
        else:
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )


# <project show and add list cloes code>

class LoginView( APIView ):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate( username=username, password=password )
        if user:
            login( request, user )
            return Response( {"Success": "Login Successfully"},status=status.HTTP_200_OK)
        return Response({"Error": "Failed"},status=status.HTTP_400_BAD_REQUEST)


class RagistationView( APIView ):
    def post(self, request):
        result={}
        username=request.data.get('username')
        password=request.data.get('password')
        email=request.data.get('email')
        user =User.objects.create_user(username=username,email=email,password=password)
        result['message']="{username} Register Successfully."
        return Response(result,status=200)



