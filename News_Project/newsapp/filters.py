from django_filters import FilterSet, ModelChoiceFilter
from .models import Post
from django import forms
import django_filters
import datetime

#
class DateInput(forms.DateInput):
    input_type = 'date'


class PostFilter(FilterSet):
    dateCreation = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'categoryType': ['exact'],
            'rating': [
               'lte',
               'gte',
           ],
       }



# class PostFilter(FilterSet):
#     class Meta:
#         model = Post
#         fields = ['title', 'categoryType', 'dateCreation', 'rating']
#         widgets = {
#             'title': ['icontains'],
#             'categoryType': ['exact'],
#             'dateCreation': DateInput(),
#             'rating': [
#                 'lte',
#                 'gte',
#             ],
#         }
#
# class PostFilter(django_filters.FilterSet):
#     dateCreation = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}))