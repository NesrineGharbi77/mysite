from django.shortcuts import render
from store.models import Product
# Create your views here.
def frontpage(request):
    products = Product.objects.all()

    print(request)
    print(request.user)
    print(request.user.is_authenticated)
    return render(request, 'core/frontpage.html', {
        'products': products
    })
def about(request):
    return render(request, 'core/about.html')