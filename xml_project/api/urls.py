# api/urls.py

from django.urls import path
from .views import HelloWorldView, MessageView, ZeekControlView, ZeekSignatureView

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('message/', MessageView.as_view(), name='message'),
    path('zeek_control/', ZeekControlView.as_view(), name='zeek_control_command'),
    path('zeek_signature/', ZeekSignatureView.as_view(), name='zeek_signature_command'),
]
