# api/serializers.py

from rest_framework import serializers

class HelloWorldSerializer(serializers.Serializer):
    message = serializers.CharField()

class MessageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    
    
class ZeekControlSerializer(serializers.Serializer):
    command = serializers.CharField(max_length=255)
