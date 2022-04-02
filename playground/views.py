from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Create your views here.
def wish_birthday(request):
    # query_set = Product.objects.all()
    # for product in query_set:
    #     print(product)

    # try:
    #     product = Product.objects.get(pk=0)
    # except:
    #     pass

    # product = Product.objects.filter(pk=0).first()

    exists = Product.objects.filter(pk=0).exists()

    return render(request, 'index.html', {"name": 'Suraj'})