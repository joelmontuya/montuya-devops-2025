from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "status": "ok"
        })

health_view = HealthView.as_view()


class BookView(APIView):
    def get(self, request, *arg, **kwargs):
        return Response(
            {
                'hello':'django'
            }
        )
    
book_view = BookView.as_view()