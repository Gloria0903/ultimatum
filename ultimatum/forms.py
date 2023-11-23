from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'image']

# class PropertyForm(forms.ModelForm):
#     class Meta:
#         model = Property
#         fields = ['name', 'address', 'price', 'description', 'photo']