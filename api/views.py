from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SchoolSerializer, ProfileSerializer
from schools.models import School
from users.models import Profile

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET':'/api/schools/'},
        {'GET':'/api/schools/id'},
        {'GET':'/api/schools/id/vote'},
        {'GET':'/api/users/token'},
        {'GET':'/api/users/token/refresh/'},

    ]

    return Response(routes)

@api_view(['GET'])
def getSchools(request):
    paginator = PageNumberPagination()
    paginator.page_size = 100  # Adjust the page size as needed
    schools = School.objects.all()
    result_page = paginator.paginate_queryset(schools, request)
    serializer = SchoolSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def getSchool(request, pk):
    school = School.objects.get(id=pk)
    serializer = SchoolSerializer(school, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getProfiles(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10  # Adjust the page size as needed
    profiles = Profile.objects.all()
    result_page = paginator.paginate_queryset(profiles, request)
    serializer = ProfileSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def getProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)