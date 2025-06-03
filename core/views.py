from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views import View
from django.conf import settings

class GoogleAuthCallback(View):
    def get(self, request):
        code = request.GET.get('code')
        if not code:
            return JsonResponse({'error': 'Missing code'}, status=400)

        token_url = "https://oauth2.googleapis.com/token"
        token_data = {
            'code': code,
            'client_id': settings.GOOGLE_CLIENT_ID,
            'client_secret': settings.GOOGLE_CLIENT_SECRET,
            'redirect_uri': settings.GOOGLE_REDIRECT_URI,
            'grant_type': 'authorization_code',
        }

        r = requests.post(token_url, data=token_data)
        token_response = r.json()
        return JsonResponse(token_response)

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SampleData
from .serializers import SampleDataSerializer

class SampleDataCreateView(APIView):
    def post(self, request):
        serializer = SampleDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)

class SampleDataListView(APIView):
    def get(self, request):
        title = request.GET.get('title')
        user_email = request.GET.get('user_email')
        queryset = SampleData.objects.all()

        if title:
            queryset = queryset.filter(title__icontains=title)
        if user_email:
            queryset = queryset.filter(user_email=user_email)

        serializer = SampleDataSerializer(queryset, many=True)
        return Response(serializer.data)
