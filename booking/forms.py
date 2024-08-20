from django import forms
from .models import CrossfitClass


class CrossfitClassForm(forms.ModelForm):
    start_time = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form-control'}),
        label='Start Time'
    )
    end_time = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form-control'}),
        label='End Time'
    )

    class Meta:
        model = CrossfitClass
        fields = ['name', 'description', 'instructor', 'start_time',
                  'end_time', 'max_participants']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'instructor': forms.TextInput(attrs={'class': 'form-control'}),
            'max_participants': forms.NumberInput(
                attrs={'class': 'form-control'}),
        }
