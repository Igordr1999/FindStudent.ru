from django import forms
import django_filters
from .models import StudentSearch, Student, StudentGroup


class SearchByPhotoURLForm(forms.ModelForm):
    class Meta:
        model = StudentSearch
        fields = ['photo_url']


class SearchByPhotoForm(forms.ModelForm):
    class Meta:
        model = StudentSearch
        fields = ['photo']


class SearchForm(forms.ModelForm):
    class Meta:
        model = StudentSearch
        fields = ['photo_url', 'photo']


class SearchParamForm(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['last_name', 'first_name', 'sex', 'student_group', 'birthday', 'user_id', 'nickname', 'city',
                  'home_town', 'has_photo', 'is_closed', 'is_deactivated']


class StudentGroupSearchParamForm(django_filters.FilterSet):
    class Meta:
        model = StudentGroup
        fields = ['name', 'group_id', 'institute', 'department']
