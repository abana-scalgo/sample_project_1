from django import forms
from .models import CMS

class CMSForm(forms.ModelForm):
    class Meta:
        model = CMS
        fields = "__all__"
        labels = {
            'heading' : "Title:",
            'content' : "Content",
            'created_date' : "Date",
        }