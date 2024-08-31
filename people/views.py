from django.core.paginator import Paginator
from django.shortcuts import render
from .filters import PersonFilter
from .models import Person

# Create your views here.

def index(request):
    persons = Person.objects.all()
    filter = PersonFilter(request.GET, queryset=persons)
    persons = filter.qs

    # Set up pagination
    paginator = Paginator(persons, 10)  # Show 10 Persons per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Preserve filter parameters in pagination links
    filter_params = request.GET.copy()
    if 'page' in filter_params:
        filter_params.pop('page')
    filter_params = filter_params.urlencode()

    context = {
        'page_obj': page_obj,
        'filter': filter,
        'filter_params': filter_params,
    }
    return render(request, 'index.html', context)
