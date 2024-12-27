from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import School
from .forms import SchoolForm, ReviewForm
from .utils import searchSchools

def schools(request):
    schools, search_query = searchSchools(request)
    
    page = request.GET.get('page')
    results = 90
    paginator = Paginator(schools, results)

    try:
        schools = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        schools = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        schools = paginator.page(page)

    context = { 'schools': schools, 'paginator': paginator, 'search_query': search_query }
    return render(request, 'schools/schools.html', context)

def school(request, pk):
    schoolObj = get_object_or_404(School, id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.school = schoolObj
            review.parent = request.user.profile
            review.save()
            schoolObj.getVoteCount
            messages.success(request, 'Your review was successfully submitted')
            return redirect('school', pk=schoolObj.id)
    return render(request, 'schools/single-school.html', {'school': schoolObj, 'form': form})

@login_required(login_url='login')
def createSchool(request):
    form = SchoolForm()
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('schools')
    context = {'form': form}
    return render(request, 'schools/school_form.html', context)

@login_required(login_url='login')
def updateSchool(request, pk):
    school = get_object_or_404(School, id=pk)
    form = SchoolForm(instance=school)
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES, instance=school)
        if form.is_valid():
            form.save()
            return redirect('schools')
    context = {'form': form}
    return render(request, 'schools/school_form.html', context)

@login_required(login_url='login')
def deleteSchool(request, pk):
    school = get_object_or_404(School, id=pk)
    if request.method == 'POST':
        school.delete()
        return redirect('schools')
    context = {'school': school}
    return render(request, 'schools/delete_school.html', context)