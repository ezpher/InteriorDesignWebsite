import django_filters
from django_filters.filters import ModelChoiceFilter
from .models import Service, Project

class ProjectFilter(django_filters.FilterSet):
    category = ModelChoiceFilter(queryset=Service.objects.all(), label="Category:")

    class Meta:
        model = Project
        fields = ['category']