from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


# Create your views here.
def hello(request):
    return render(request, 'hello.html', {'name': 'eugene'})
    # return HttpResponse('<h2>Hello<h2>')


def get_smthng(request):
    # queryset = Product.objects.filter(unit_price__gt=20)
    # queryset = Product.objects.filter(price__range=(200, 8030))
    # queryset = Product.objects.filter(collection_id__exact=1)
    queryset = Product.objects.filter(description__iexact='phone')
    return render(request, 'hello.html', {'name': 'Eugene',
                                          'products': list(queryset)})
