from django_filters.widgets import RangeWidget

from .models import Posts
import django_filters
from django_filters import rest_framework as filters


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PostsFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name="category__en_title", lookup_expr="in")
    created_date = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY-DD-MM'}))

    class Meta:
        model = Posts
        fields = "category created_date".split()