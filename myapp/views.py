from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.conf import settings
from datetime import time
from .serializers import InputSerializer


@api_view(['POST'])
def MyView(request):
    serializer = InputSerializer(data = request.data)
    if serializer.is_valid():
        subject = serializer.validated_data.get('subject')
        message = serializer.validated_data.get('message')
        recipient = serializer.validated_data.get('recipient')
    message_from = settings.EMAIL_HOST_USER
    message_to = [settings.EMAIL_HOST_USER,recipient]

    send_mail(subject,message,message_from,message_to,fail_silently=False)

    return JsonResponse({
        'email-data':{
            'subject':subject,
            'message':message,
            'message_from':message_from,
            'message_to':message_to
        }
    })