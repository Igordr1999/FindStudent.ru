from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.status import (HTTP_200_OK,)
from rest_framework.response import Response

from .forms import ProfileCreationForm, ProfileLoginForm


class Registration(generic.CreateView):
    form_class = ProfileCreationForm
    success_url = reverse_lazy('login')
    template_name = 'profiles/registration.html'


class Login(generic.FormView):
    form_class = ProfileLoginForm
    success_url = reverse_lazy('home')
    template_name = 'profiles/login.html'


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)
