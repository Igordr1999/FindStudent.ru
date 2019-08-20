from django import forms
import django_filters
from .models import BugTrackerReport


class ReportForm(forms.ModelForm):
    class Meta:
        model = BugTrackerReport
        fields = ['product', 'title', 'description', 'playback_steps', 'expected_result', 'factual_result',
                  'type_report', 'tags', 'priority', 'screenshot']
