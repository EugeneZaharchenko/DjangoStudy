from django.db.models import Q, F, Value, FloatField, Func, ExpressionWrapper
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from django.db.models.functions import Concat
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, OrderItem, Order, Customer
from tags.models import TaggedItem


# Create your views here.
def hello(request):
    tags_set = TaggedItem.objects.get_tags_for(Product, 1)

    queryset = Product.objects.only('id', 'title')
    # queryset = Product.objects.defer('description') - 'description' will be excluded
    customers = Customer.objects.annotate(
        full_name=Value('eugene'),
        is_new=Value(True),
        new_id=F('id') * 10)

    discounted_price = ExpressionWrapper(
        F('price') * 0.75,
        output_field=FloatField())
    discounted_query = Product.objects.annotate(
        discounted_price=discounted_price)

    # fulL_name_customers = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )
    fulL_name_customers = Customer.objects.annotate(
        full_name=Concat('first_name', Value(' '), 'last_name')
    )
    queryset = Customer.objects.annotate(
        orders_count=Count('order')
    )

    # print(customers)
    # print(queryset)
    print(list(discounted_query))
    return render(request, 'hello.html', {'name':
                                              fulL_name_customers[0].full_name,
                                          'tags': list(tags_set)})
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
    # queryset = Product.objects.values('id', 'title', 'collection__title')
    # queryset = Product.objects.select_related('collection').all()  #  INNER JOIN "collection"
    queryset = Product.objects.prefetch_related('promotions').select_related(
        'collection').all()  # INNER JOIN, use 'prefetch' when have many-to-many relationship
    # queryset = Product.objects.filter(id__exact=1).first()
    # product = Product.objects.order_by('price')[0]
    # product = Product.objects.earliest('price')
    # product = Product.objects.latest('inventory')
    orders = Order.objects.select_related('customer').order_by('-placed_at')[:3]
    if queryset:
        return render(request, 'hello.html', {'name': 'Eugene',
                                              'products': list(queryset),
                                              'orders': list(orders)})
    # return render(request, 'hello.html', {'name': 'Eugene',
    #                                       'product': product})


def get_order_items(request):
    queryset = Product.objects.filter(
        id__in=OrderItem.objects.values('product_id').distinct()).order_by('-price')
    if queryset:
        return render(request, 'order_items.html', {'name': 'Eugene',
                                                    'products': list(queryset)})


def get_aggregations(request):
    queryset = (Product.objects.filter(collection__id=1).aggregate(count=Count('id'),
                                                                   min_price=Min('price'),
                                                                   max_price=Max('price'),
                                                                   avg_price=Avg('price')))
    return render(request, 'aggregations.html', {'name': 'Eugene',
                                                 'result': queryset})
