from django.shortcuts import render, get_object_or_404
from .models import Product, Ingredient

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
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
