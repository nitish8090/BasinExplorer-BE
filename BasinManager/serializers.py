from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField
from .models import JunctionPoint, RiverStream, Watershed


class JunctionPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = JunctionPoint
        geo_field = "geom"
        fields = '__all__'


class RiverStreamSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RiverStream
        geo_field = "geom"
        fields = '__all__'


class WatershedSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Watershed
        geo_field = "geom"
        fields = '__all__'
