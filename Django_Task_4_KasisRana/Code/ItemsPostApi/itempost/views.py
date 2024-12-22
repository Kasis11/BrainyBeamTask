from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

class ItemCreateAPIView(APIView):
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            item = serializer.save()
            # Get the count of saved records
            count = Item.objects.count()
            return Response({
                'data': serializer.data,
                'count': count
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
