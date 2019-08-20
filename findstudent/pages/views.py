from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy

from .forms import ReportForm


def home_page(request):
    return render(request, 'pages/home.html')


def about_page(request):
    return render(request, 'pages/about.html')


def team_page(request):
    return render(request, 'pages/our_team.html')


def contacts_page(request):
    return render(request, 'pages/contacts.html')


def get_started(request):
    return render(request, 'pages/get_started.html')


class BugTrackerCreate(LoginRequiredMixin, CreateView):
    form_class = ReportForm
    template_name = 'pages/bugtracker_create_report.html'
    success_url = reverse_lazy('bugtracker_create')
