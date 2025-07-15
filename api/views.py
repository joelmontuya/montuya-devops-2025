from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import status

class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "status": "ok"
        })

health_view = HealthView.as_view()

#
# /api/books - All method (GET, POST, UPDATE, DELETE)
#

class BookView(APIView):
    def get(self, request, *arg, **kwargs):
        all_books = Book.objects.all()
        serializers = BookSerializer(all_books, many=True)
        return Response(serializers.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = BookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #### Another approach for handling incorrect format
        #  if not serializer.is_valid():
        #  return Response('The data is invalid.', status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            'status':'ok',
            'data':serializer.data
            })
    
    
book_view = BookView.as_view()