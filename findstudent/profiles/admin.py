from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.admin import TokenAdmin

from .forms import ProfileCreationForm, ProfileChangeForm
from .models import Profile


class ProfileAdmin(UserAdmin):
    model = Profile
    add_form = ProfileCreationForm
    form = ProfileChangeForm


admin.site.register(Profile, ProfileAdmin)
TokenAdmin.raw_id_fields = ('user',)


"""
@admin.register(PremiumPlan)
class StudentPhotoAdmin(admin.ModelAdmin):
    list_display = ['name', 'interval_days', 'amount', 'request_limit_per_second',
                    'request_limit_per_minute', 'request_limit_per_hour',
                    'request_limit_per_day', 'request_limit_per_month',
                    'active', 'API_access']


@admin.register(PremiumProfile)
class StudentPhotoAdmin(admin.ModelAdmin):
    list_display = ['owner', 'premium_plan', 'start_date', 'end_date']
    list_filter = ['owner']
    
"""
