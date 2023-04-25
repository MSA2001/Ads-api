from rest_framework.views import APIView
from .models import Ad
from .serializers import AdSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class AdListView(APIView):
    serializer_class = AdSerializer

    def get(self, request):
        queryset = Ad.objects.filter(is_public=True)
        serializer = AdSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)