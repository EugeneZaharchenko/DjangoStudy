from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, OrderItem


# Create your views here.
def hello(request):
    return render(request, 'hello.html', {'name': 'eugene'})
    # return HttpResponse('<h2>Hello<h2>')


def get_products(request):
    # queryset = list()
    # queryset = Product.objects.filter(unit_price__gt=20)
    # queryset = Product.objects.filter(price__range=(200, 8030))
    # queryset = Product.objects.filter(collection_id__exact=1)
    # queryset = Product.objects.filter(description__iexact='phone')
    # queryset = Product.objects.filter(inventory__lt=16, price__gt=100000)
    # queryset = Product.objects.filter(Q(inventory__lte=14) | Q(price__in=(6500, 6200)))
    # queryset = Product.objects.filter(inventory=F('price'))
    # queryset = Product.objects.order_by('price', '-description').reverse()[:5]
    queryset = Product.objects.values('id', 'title', 'collection__title')
    # product = Product.objects.order_by('price')[0]
    # product = Product.objects.earliest('price')
    # product = Product.objects.latest('inventory')
    if queryset:
        return render(request, 'hello.html', {'name': 'Eugene',
                                              'products': list(queryset)})
    # return render(request, 'hello.html', {'name': 'Eugene',
    #                                       'product': product})


def get_order_items(request):
    queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('-price')
    if queryset:
        return render(request, 'order_items.html', {'name': 'Eugene',
                                                    'products': list(queryset)})
