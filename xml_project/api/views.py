from django.shortcuts import render

# Create your views here.
# hello/views.py
import uuid
import os


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloWorldSerializer, MessageSerializer, ZeekControlSerializer, ZeekSignatureSerializer
from .service.zeek_command import ZeekCommand
from .config import config
from .data_transfer_object.response import ResponseData


class HelloWorldView(APIView):
    def get(self, request):
        data = {"message": config.GREETING_NAME}
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
            try:
                command = serializer.validated_data['command']
                
                zeek = ZeekCommand()
                result = zeek.run_command(command, zeekctl_path=config.ZEEKCTL_PATH)
                print(result)
                
                response_data = {
                    "is_success": True,
                    "message": "success",
                    "error_message": "",
                    "detail" : result
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            except Exception as e:
                print(f"An error occurred: {e}")
                response_data = {
                    "is_success": False,
                    "message": "failure",
                    "error_message" : f"An error occurred: {e}",
                    "detail" : ""
                }
                Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ZeekSignatureView(APIView):
    def post(self, request):
        serializer = ZeekSignatureSerializer(data=request.data)
        if serializer.is_valid():
            try:
                sig_ip_proto = serializer.validated_data['sig_ip_proto']
                sig_dst_port = serializer.validated_data['sig_dst_port']
                sig_payload = serializer.validated_data['sig_payload']
                event_message = serializer.validated_data['sig_event']
                unique_id = uuid.uuid4()
                pcap_file = config.PCAP_FILE_PATH
                file_script_directory = "/home/wahyu/python/zeek-signature/signature"
                execution_path = "/home/wahyu/python/zeek-signature/logs"
                
                sig_event = f""" "{event_message}" """
                signature_content = """
                signature signature_""" + format(unique_id) + """{
                    ip-proto == """ + format(sig_ip_proto) + """
                    dst-port == """ + format(sig_dst_port) + """
                    payload """ + format(sig_payload) + """
                    event """ + format(sig_event) + """
                }
                """
                
                sig_file_name = f"sig_file_name_{unique_id}.sig"
                zeek_file_name = f"sig_loader_file_name_{unique_id}.zeek"
                
                zeek_script_content = f"""
                @load-sigs {os.path.join(file_script_directory, sig_file_name)}
                """

                zeek = ZeekCommand()
                zeek.create_zeek_script_file(sig_file_name, zeek_file_name, signature_content, zeek_script_content, file_script_directory)
                zeek.execute_pcap(pcap_file, zeek_file_name, execution_path, file_script_directory)
            
                response_data = ResponseData()
                return Response(response_data.to_dict(), status=status.HTTP_201_CREATED)
            except Exception as e:
                print(f"An error occurred: {e}")
                response_data = ResponseData(False, "failure", f"An error occurred: {e}")
                Response(response_data.to_dict(), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)