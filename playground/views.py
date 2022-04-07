from os import stat
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from store.models import Product, OrderItem, Order
import datetime


# Create your views here.
def wish_birthday(request):
    # query_set = Product.objects.all()
    # for product in query_set:
    #     print(product)

    #product = Product.objects.count()

    # try:
    #     product = Product.objects.get(pk=0)
    # except:
    #     pass

    # product = Product.objects.filter(pk=0).first()
    #exists = Product.objects.filter(pk=0).exists()

    # queryset = Product.objects.filter(unit_price__gt = 20)
    # queryset = Product.objects.filter(unit_price__range= (20, 30))
    # queryset = Product.objects.filter(title__icontains = 'coffee')
    # queryset = Product.objects.filter(title__startswith = 'coffee')
    # queryset = Product.objects.filter(collection__id__gt = 1)
    # queryset = Product.objects.filter(collection__id__range = 1)
    # queryset = Product.objects.filter(description__isnull = True)
    # queryset = Product.objects.filter(last_update__year = 2021)
    # queryset = Product.objects.filter(last_update__date__gt = datetime.date(2021, 3, 3))

    #Q Object
    # queryset = Product.objects.filter(Q(inventory__lt = 10) | Q(unit_price__lt = 20))

    #F Object
    # queryset = Product.objects.filter(inventory = F('collection__id'))

    #Sorting 
    # queryset = Product.objects.order_by('unit_price', '-title').reverse()
    # queryset = Product.objects.filter(collection__id = 1).order_by('unit_price')
    # product = Product.objects.filter.order_by('unit_price')[0]
    # ===
    #queryset = Product.objects.earliest('unit_price')
    #queryset = Product.objects.latest('unit_price')

    #Selecting Fields to Query
    # queryset = Product.objects.values('id', 'title', 'collection__id')
    ##Select products that have been ordered and sort them by title
    # queryset = Product.objects.filter(id__in = OrderItem.objects.values('product_id').distinct()).order_by('title')

    #select_related
    # queryset = Product.objects.select_related('collection').all()

    #prefetch_related
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()


    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    stats = Product.objects.aggregate(count = Count('id'), min = Min('unit_price'), max = Max('unit_price'), avg = Avg('unit_price'), sum = Sum('unit_price'))

    return render(request, 'index.html', {"name": "Suraj", "stats": stats})