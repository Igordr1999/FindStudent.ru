from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField


class ProfileManager(UserManager):
    pass


class Profile(AbstractUser):
    objects = ProfileManager()


"""
class PremiumPlan(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name=_('Name'))
    description = models.CharField(max_length=256, verbose_name=_('description'))
    interval_days = models.IntegerField(verbose_name=_('Interval days'))
    amount = models.FloatField(verbose_name=_('Amount'))
    request_limit_per_second = models.IntegerField(verbose_name=_('Request limit per second'))
    request_limit_per_minute = models.IntegerField(verbose_name=_('Request limit per minute'))
    request_limit_per_hour = models.IntegerField(verbose_name=_('Request limit per hour'))
    request_limit_per_day = models.IntegerField(verbose_name=_('Request limit per day'))
    request_limit_per_month = models.IntegerField(verbose_name=_('Request limit per month'))
    active = models.BooleanField(verbose_name=_('Amount'))
    API_access = models.BooleanField(verbose_name=_('API access'))
    icon = ProcessedImageField(upload_to='profiles/PremiumPlan/',
                               format='PNG',
                               options={'quality': 60},
                               null=True,
                               verbose_name=_('Icon'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Premium Plans')
        verbose_name_plural = _('Premium Plans')
        ordering = ["name"]


class PremiumProfile(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('Owner'))
    premium_plan = models.ForeignKey(PremiumPlan, on_delete=models.CASCADE, verbose_name=_('Premium plan'))
    start = models.DateTimeField(auto_now_add=True, verbose_name=_('Start date'))
    end = models.DateTimeField(verbose_name=_('End date'))

    def __str__(self):
        return self.premium_plan.name

    class Meta:
        verbose_name = _('Premium account')
        verbose_name_plural = _('Premium accounts')
        ordering = ["-start_date"]


class PremiumMethod(models.Model):
    pass

class PremiumRequest(models.Model):
    account = models.ForeignKey(PremiumProfile, on_delete=models.CASCADE, verbose_name=_('Account'))
    record_create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Record create date'))

"""
