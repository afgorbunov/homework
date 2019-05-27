from django.forms.models import ModelForm

from mainapp.models import Good


class GoodCreateForm(ModelForm):
    
    class Meta:
        model = Good
        fields = ("__all__",)
