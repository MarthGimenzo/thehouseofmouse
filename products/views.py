from django.shortcuts import render
from .models import Product

# Create your views here.
def listing_view(request, *args, **kwargs):
    """ view specific product details """
    product = Product.objects.get(id=2)
    num_in_stock = product.num_in_stock

    stock_arr = []
    for i in range(num_in_stock):
        stock_arr.append(i)

    context = {
        'product': product,
        'stock_arr': stock_arr,
        'num_in_stock': num_in_stock,
    }
    return render(request, "listing.html", context)

def results_view(request, *args, **kwargs):
    """ results_view can be used for search results, category or favourites """
    return render(request, "results.html")

def all_products_view(request, *args, **kwargs):
    """ displays all products """
    context = {
        'products': Product.objects.all()
    }
    return render(request, "all_products.html", context)