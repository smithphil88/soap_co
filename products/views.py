from django.shortcuts import render, redirect, reverse,  get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Ingredient

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show one product """

    product = get_object_or_404(Product, pk=product_id)

    print(f"Product: {product.name}")

    ingredients = product.ingredients.all()
    if ingredients.exists():
        for ingredient in ingredients:
            print(f"Ingredient: {ingredient.name}, Image URL: {ingredient.image.url if ingredient.image else 'No Image'}")
    else:
        print("No ingredients linked to this product.")

    context = {
        'product': product,
        'ingredients': ingredients,
    }

    return render(request, 'products/product_detail.html', context)
