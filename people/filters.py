import django_filters
from django import forms
from .models import Person

class PersonFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(
        field_name='id', 
        label='ID',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    name = django_filters.CharFilter(
        lookup_expr='icontains', 
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    age = django_filters.NumberFilter(
        field_name='age', 
        label='Age',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    sex = django_filters.ChoiceFilter(
        choices=Person._meta.get_field('sex').choices,
        label='Sex',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    created_at = django_filters.DateFilter(
        field_name='created_at', 
        lookup_expr='exact', 
        label='Date',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    class Meta:
        model = Person
        fields = ['id', 'name', 'age', 'sex','created_at']
