from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('about/', views.about_page, name="about"),
    path('team/', views.team_page, name="team"),
    path('contacts/', views.contacts_page, name="contacts"),
    path('get-started/', views.get_started, name="get_started"),
    path('bugtracker/create/', views.BugTrackerCreate.as_view(), name="bugtracker_create"),
]
