from django.shortcuts import render

from mainapp.models import Product, ProductCategory

links_menu = [
    {'href': 'index', 'name': 'Домой', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
]


def products(request):
    title = 'Продукты'

    products_ = Product.objects.all() #.filter(category__name__in=['Бобры', 'Джинсы']).order_by('price')  # [:2]
    categories = ProductCategory.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_,
        'categories': categories,
    }
    return render(request, 'products.html', context)


def product(request):
    return render(request, 'product.html')
