from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product
from django.http import JsonResponse
# Create your views here.


def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    request.session.modified = True
    return redirect(redirect_url)


def update_bag(request, item_id):
    """ Update the quantity of the specified product in the bag """

    try:
        quantity = int(request.POST.get('quantity', 1))  # Get quantity from POST
        bag = request.session.get('bag', {})

        if quantity > 0:
            bag[item_id] = quantity  # Update the item quantity
        else:
            bag.pop(item_id, None)  # Remove item if quantity is 0

        request.session['bag'] = bag
        request.session.modified = True  # Ensure session updates

        return redirect('view_bag')  # Redirect to shopping bag page

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def remove_from_bag(request, item_id):
    """Remove an item from the shopping bag"""
    try:
        bag = request.session.get('bag', {})

        if item_id in bag:
            del bag[item_id]  # Remove the item from the session bag

        request.session['bag'] = bag
        request.session.modified = True  # Ensure session updates

        return redirect('view_bag')

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
