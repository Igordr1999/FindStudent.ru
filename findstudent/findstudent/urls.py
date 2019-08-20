from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views as drf

from data import views, viewsets

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('profile/', include('profiles.urls')),
    path('accounts/', include("account.urls")),
    path('data/', include('data.urls')),

    path('api/GetToken/', drf.obtain_auth_token, name="get_token"),
    path('api/ContinentListView/', viewsets.ContinentListView.as_view()),
    path('api/CountryListView/', viewsets.CountryListView.as_view()),
    path('api/TimezoneListView/', viewsets.TimezoneListView.as_view()),
    path('api/CityListView/', viewsets.CityListView.as_view()),
    path('api/UniversityListView/', viewsets.UniversityListView.as_view()),
    path('api/RoomListView/', viewsets.RoomListView.as_view()),
    path('api/InstituteListView/', viewsets.InstituteListView.as_view()),
    path('api/DepartmentListView/', viewsets.DepartmentListView.as_view()),
    path('api/LecturerListView/', viewsets.LecturerListView.as_view()),
    path('api/PeriodListView/', viewsets.PeriodListView.as_view()),
    path('api/StudentGroupListView/', viewsets.StudentGroupListView.as_view()),
    path('api/SexListView/', viewsets.SexListView.as_view()),
    path('api/EmotionTypeListView/', viewsets.EmotionTypeListView.as_view()),
    path('api/LandmarkTypeListView/', viewsets.LandmarkTypeListView.as_view()),
    path('api/StudentListView/', viewsets.StudentListView.as_view()),
    path('api/StudentPhotoListView/', viewsets.StudentPhotoListView.as_view()),
    path('api/StudentSearchCodeView/', viewsets.StudentSearchCodeView.as_view()),
    path('api/StudentSearchListView/', viewsets.StudentSearchListView.as_view()),
    path('api/StudentSearchRetrieveView/<code>/', viewsets.StudentSearchRetrieveView.as_view()),
    path('api/StudentSearchCreateByURLView/', viewsets.StudentSearchCreateByURLView.as_view()),
    path('api/StudentSearchCreateByPhotoView/', viewsets.StudentSearchCreateByPhotoView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
