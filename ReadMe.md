## Basin Explorer
#### Author: Nitish Patel
|Build Status|

![Project Image](https://github.com/nitish8090/BasinExplorer-BE/blob/master/preview.png?raw=true)

BasinExplorerBE is the BackEnd of the Basin Explorer project. The project is built using [Django](https://github.com/django/django), [Django REST Framework](https://github.com/encode/django-rest-framework), [Django-REST-Framework-GIS](https://github.com/openwisp/django-rest-framework-gis), etc. 

To see a live demo, go to:
**[Project Link!](https://www.nitishpatel.in/preview/basinexplorer)**

<hr>

### Purpose
The project has following purpose:
1. To provide Authentication to user access in frontend.
2. To provide REST API to BasinExplorer FrontEnd.


### 1. Authentication
The Authentication system is based on DRF's Token authentication system and has two types of access methods, Admin Level and User level. User's don't have the access to the Geometry APIs where as the admin's have.

### 2. REST APIs
The REST APIs respond with geometry sent as GeoJSON. Three kinds of data are being provided:
1. Point Data (River Junctions)
2. Line Data (River Streams)
3. Polygon Data (Basin Perimeters)

The serializer being used in `GeoFeatureModelSerializer` which gives the data in GeoJSON format rather than normal JSON. 

These APIs are consumed by front end where open layer is using these data to create layers on the map.

The Data is saved in a Postgres database with postgis extension installed. 

This project was created for demonstration of my skills.

<hr>

References:
- 

