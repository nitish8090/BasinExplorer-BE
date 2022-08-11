from django.contrib.gis.db import models


class JunctionPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    arcid = models.FloatField(blank=True, null=True)
    grid_code = models.FloatField(blank=True, null=True)
    from_node = models.FloatField(blank=True, null=True)
    to_node = models.FloatField(blank=True, null=True)
    orig_fid = models.FloatField(blank=True, null=True)
    geom = models.PointField(srid=3857, blank=True, null=True)


class RiverStream(models.Model):
    gid = models.AutoField(primary_key=True)
    arcid = models.FloatField(blank=True, null=True)
    grid_code = models.FloatField(blank=True, null=True)
    from_node = models.FloatField(blank=True, null=True)
    to_node = models.FloatField(blank=True, null=True)
    geom = models.MultiLineStringField(srid=3857, blank=True, null=True)


class Watershed(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.FloatField(blank=True, null=True)
    gridcode = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=3857, blank=True, null=True)

