from django.urls import path

from . import views

urlpatterns = [
    path('continents/', views.ContinentListView.as_view(), name="continents"),
    path('countries/', views.CountryListView.as_view(), name="countries"),
    path('timezones/', views.TimezoneListView.as_view(), name="timezones"),
    path('cities/', views.CityListView.as_view(), name="cities"),
    path('universities/', views.UniversityListView.as_view(), name="universities"),

    path('group/<group_name>/', views.StudentByGroupListView.as_view(), name="group_page"),
    path('student/<int:user_id>/', views.StudentDetailView.as_view(), name="student_page"),
    path('university/<abbr>/', views.UniversityDetailView.as_view(), name="university"),
    path('search/', views.SearchByImageView.as_view(), name="photo_search"),
    path('search_by_photo_url/', views.SearchByImageURLView.as_view(), name="search_by_photo_url"),
    path('my_searches/', views.MySearchesView.as_view(), name="my_searches"),
    path('student_search/', views.StudentSearchView.as_view(), name="student_search"),
    path('search/<code>/', views.StudentSearchDetailView.as_view(), name="search_code"),
    path('student_group_search/', views.StudentGroupSearchView.as_view(), name="student_group_search"),

    path('create_student_group/<name>/<int:group_id>/<int:institute_id>/',
         views.data_create_student_group, name="create_student_group"),
    path('create_student_photos/<int:user_id>/', views.data_create_student_photos),
    path('data_create_student_photos_by_group/<int:group_id>/', views.data_create_student_photos_by_group),
    path('data_index_student_photos_by_group/<int:group_id>/', views.data_index_student_photos_by_group),
    path('data_create_all_by_group/<name>/<int:group_id>/<int:institute_id>/', views.data_create_all_by_group),
]
