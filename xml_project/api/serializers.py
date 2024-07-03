# api/serializers.py

from rest_framework import serializers

class HelloWorldSerializer(serializers.Serializer):
    message = serializers.CharField()

class MessageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    
    
class ZeekControlSerializer(serializers.Serializer):
    command = serializers.CharField(max_length=255)

class ZeekSignatureSerializer(serializers.Serializer):
    sig_ip_proto = serializers.CharField(required=True, allow_blank=False)
    sig_dst_port = serializers.CharField(required=True, allow_blank=False)
    sig_payload = serializers.CharField(required=True, allow_blank=False)
    sig_event = serializers.CharField(required=True, allow_blank=False)