from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.urls import reverse_lazy
from profiles.models import Profile
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from django_filters.views import FilterView

from .models import Continent, Country, Timezone, City, Student, StudentGroup, StudentPhoto,\
    University, Institute, Department, Lecturer, StudentSearch
from .creater import create_student_group, create_student_photos_by_user_id, create_student_photos_by_group, \
    index_student_photos_by_group, student_search, get_search_details
from .forms import SearchByPhotoURLForm, SearchByPhotoForm, SearchParamForm, StudentGroupSearchParamForm, SearchForm


def change_lang(request, code):
    request.session[LANGUAGE_SESSION_KEY] = code
    return HttpResponse("OK")


def data_home(request):
    return render(request, 'base_data.html', {})


class ContinentListView(ListView):
    model = Continent
    template_name = "data/continents.html"


class CountryListView(ListView):
    model = Country
    paginate_by = 10
    template_name = "data/countries.html"


class TimezoneListView(ListView):
    model = Timezone
    paginate_by = 20
    template_name = "data/timezones.html"


class CityListView(ListView):
    model = City
    paginate_by = 20
    template_name = "data/cities.html"


class UniversityListView(ListView):
    model = University
    paginate_by = 20
    template_name = "data/universities.html"


class StudentByGroupListView(ListView):
    paginate_by = 50
    template_name = "data/students_by_group.html"

    def get_queryset(self):
        return Student.objects.filter(student_group__name_en=self.kwargs['group_name'])

    def get_context_data(self, **kwargs):
        context = super(StudentByGroupListView, self).get_context_data(**kwargs)
        context['student_group'] = StudentGroup.objects.get(name_en=self.kwargs['group_name'])
        return context


class UniversityDetailView(DetailView):
    model = University
    slug_field = "abbr_en"
    slug_url_kwarg = "abbr"
    template_name = "data/university.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['institutes'] = Institute.objects.filter(university=self.get_object())
        context['departments'] = Department.objects.filter(institute__university=self.get_object())
        context['lecturers'] = Lecturer.objects.filter(department__institute__university=self.get_object())
        context['groups'] = StudentGroup.objects.filter(institute__university=self.get_object())
        return context


class StudentDetailView(DetailView):
    model = Student
    slug_field = "user_id"
    slug_url_kwarg = "user_id"
    template_name = "data/student.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = StudentPhoto.objects.filter(owner=self.get_object())
        return context


def data_create_student_group(request, name, group_id, institute_id):
    create_student_group(name=name, group_id=group_id, institute_id=institute_id)
    return HttpResponse("OK. Group:{}; VK ID:{}; Institute ID:{};".format(name, group_id, institute_id))


def data_create_student_photos(request, user_id):
    create_student_photos_by_user_id(user_id=user_id)
    return HttpResponse("OK")


def data_create_student_photos_by_group(request, group_id):
    create_student_photos_by_group(group_id=group_id)
    return HttpResponse("OK")


def data_index_student_photos_by_group(request, group_id):
    index_student_photos_by_group(group_id=group_id)
    return HttpResponse("OK")


def data_create_all_by_group(request, name, group_id, institute_id):
    create_student_group(name=name, group_id=group_id, institute_id=institute_id)
    create_student_photos_by_group(group_id=group_id)
    index_student_photos_by_group(group_id=group_id)
    return HttpResponse("OK")


class StudentSearchView(FilterView):
    template_name = "data/search_student.html"
    filterset_class = SearchParamForm


class StudentGroupSearchView(FilterView):
    template_name = "data/search_group.html"
    filterset_class = StudentGroupSearchParamForm


class StudentSearchDetailView(DetailView):
    model = StudentSearch
    slug_field = "code"
    slug_url_kwarg = "code"
    template_name = "data/result_search.html"


class SearchByImageView(LoginRequiredMixin, CreateView):
    form_class = SearchByPhotoForm
    template_name = 'data/search_photo.html'
    success_url = reverse_lazy('photo_search')

    def form_valid(self, form):
        form_url = form.save(commit=False)
        form_url.owner = Profile.objects.get(id=self.request.user.id)
        form_url.save()

        student_search(photo_id=form_url.id)
        get_search_details(search_code=form_url.code)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SearchByImageView, self).get_context_data(**kwargs)
        context['my_searches'] = StudentSearch.objects.filter(owner_id=self.request.user.id)[:5]
        return context


class SearchByImageURLView(LoginRequiredMixin, CreateView):
    form_class = SearchByPhotoURLForm
    template_name = 'data/search_photo_url.html'
    success_url = reverse_lazy('search_by_photo_url')

    def form_valid(self, form):
        form_url = form.save(commit=False)
        form_url.owner = Profile.objects.get(id=self.request.user.id)
        form_url.save()

        student_search(photo_id=form_url.id)
        get_search_details(search_code=form_url.code)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SearchByImageURLView, self).get_context_data(**kwargs)
        context['my_searches'] = StudentSearch.objects.filter(owner_id=self.request.user.id)[:5]
        return context


class MySearchesView(LoginRequiredMixin, ListView):
    model = StudentSearch
    paginate_by = 10
    template_name = "data/my_searches.html"

    def get_queryset(self, *args, **kwargs):
        return StudentSearch.objects.filter(owner_id=self.request.user.id)
