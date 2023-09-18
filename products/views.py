from django.shortcuts import render
from products.models import Product
# Create your views here.


def get_product(request, slug):
    try:
        single_product = Product.objects.get(slug=slug)
        context = {'single_product' : single_product }

        if request.GET.get('size'):
            size = request.GET['size']
            # print(size)

            price = single_product.get_product_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price
            # print(price)

        return render(request,'product/products.html',context)

    except Exception as e:
        print("ERROR:>",e)
        
        return render(request,'404.html')
    
