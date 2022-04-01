from django import forms
from monitor.models import IOT
class IOTForm(forms.ModelForm):
    class Meta:
        model = IOT
        fields = "__all__" 
