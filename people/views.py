from django.shortcuts import render
from .filters import PersonFilter
from .models import Person

# Create your views here.

def index(request):
    persons = Person.objects.all()
    filter = PersonFilter(request.GET, queryset=persons)
    persons = filter.qs
    context = {
        'persons': persons,
        'filter': filter
    }
    return render(request, 'index.html', context)
