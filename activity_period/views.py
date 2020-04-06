from django.shortcuts import render

#below modules are imported for using RestAPI's , models , serializers
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class User_view(APIView):
	def get( self, 	request):
		user = User.objects.all()
		serializer = UserSerializer(user , many = True)
		return Response(serializer.data)
	def post(self, request):
		serializer = User_Serializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class User_view(APIView):
# 	def get( self, 	request):
# 		user = User.objects.all()
# 		serializer = User_Serializer(user , many = True)
# 		return Response(serializer.data)

