from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from bike.models import Station
# Create your views here.

def bikesTable(request):
    qs = Station.objects.order_by('-timestamp').all()
    paginator = Paginator(qs, 10)
    page = request.GET.get("page", 1)
    try:
        show_lines = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_lines = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_lines = paginator.page(paginator.num_pages)
    return HttpResponse(render(request,'bike/table.html', {"qs":show_lines}))
