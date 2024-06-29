from django.shortcuts import render

# Create your views here.
# hello/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloWorldSerializer, MessageSerializer, ZeekControlSerializer
from .service.zeek_command import ZeekCommand

class HelloWorldView(APIView):
    def get(self, request):
        data = {"message": "Hello World"}
        serializer = HelloWorldSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MessageView(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            age = serializer.validated_data['age']
            response_data = {
                'greeting': f"Hello, {name}!",
                'age_in_10_years': age + 10,
                'message': f"In 10 years, you will be {age + 10} years old."
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ZeekControlView(APIView):
    def post(self, request):
        serializer = ZeekControlSerializer(data=request.data)
        if serializer.is_valid():
            command = serializer.validated_data['command']
            
            zeek = ZeekCommand()
            result = zeek.run_command(command)
            print(result)
            
            response_data = {
                "message": "success",
                "detail" : result
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)