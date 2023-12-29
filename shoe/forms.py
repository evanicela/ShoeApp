from django import forms
from shoe.models import Shoe


class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = "__all__"

