from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product
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
    queryset = Product.objects.filter(inventory = F('collection__id'))

    return render(request, 'index.html', {"name": "Suraj", "products": list(queryset)})