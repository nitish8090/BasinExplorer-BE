from rest_framework.viewsets import ModelViewSet
from rest_framework.response import  Response
from .models import JunctionPoint, RiverStream, Watershed
from .serializers import JunctionPointSerializer, RiverStreamSerializer, WatershedSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class JunctionPointViewSet(ModelViewSet):
    queryset = JunctionPoint.objects.all()
    serializer_class = JunctionPointSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def list(self, request, *args, **kwargs):
        filter_dict = {}
        if 'grid_code' in request.GET.keys():
            filter_dict = {'grid_code': request.GET.get('grid_code')[0]}

        queryset = JunctionPoint.objects.filter(**filter_dict)
        serializer_class = JunctionPointSerializer(queryset, many=True)

        return Response(serializer_class.data)


class RiverStreamViewSet(ModelViewSet):
    queryset = RiverStream.objects.all()
    serializer_class = RiverStreamSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]


class WatershedViewSet(ModelViewSet):
    queryset = Watershed.objects.all()
    serializer_class = WatershedSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
