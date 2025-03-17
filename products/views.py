from django.shortcuts import render, redirect, reverse,  get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product, Ingredient, Category
from .forms import ProductForm

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sort = request.GET['sort']
            direction = request.GET.get('direction', 'asc')
            if sort == 'name':
                products = products.order_by('name' if direction == 'asc' else '-name')
            elif sort == 'price':
                products = products.order_by('price' if direction == 'asc' else '-price')

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

            if not products.exists():
                messages.warning(request, "No products found matching your search.")

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
