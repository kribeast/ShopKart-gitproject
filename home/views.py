from django.shortcuts import render, get_object_or_404
from products.models import Product, Category

# Create your views here.
def index(request):

    context = {'products': Product.objects.all()}
    return render(request,'home/home.html',context)

def store(request, category_slug=None):
    try:
        products = None
        category = None

        if category_slug != None:
            categories = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=categories)
            product_count = products.count()

        else:

            products = Product.objects.all()
            product_count = products.count()
        
        context = {

            'products': products,
            'product_count' : product_count
        
        }
        return render(request, 'home/store.html',context)
    except:
        return render(request,'404.html')
    
# def product_detail(request,category_slug, product_slug):
#     try:
#         single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
#     except Exception as e:
#         raise e
    
#     context = {
#         'single_product': single_product
#     }
#     return render(request,'product/products.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(product_name__icontains=keyword)
            product_count = products.count()

    context = {
        'products': products,
        'product_count' : product_count,
    }
    return render(request, 'home/store.html',context)