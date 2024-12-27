from .models import School
from django.db.models import Q

def searchSchools(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    schools = School.objects.filter(
        Q(establishment_name__icontains=search_query) | 
        Q(establishment_number__icontains=search_query) | 
        Q(town__icontains=search_query))
    return schools, search_query