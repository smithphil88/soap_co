from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product
from django.http import JsonResponse
# Create your views here.


def view_bag(request):
    """ A view to return the shopping bag page with free soap offer check """

    bag = request.session.get('bag', {})
    total_items = sum(bag.values())
    free_soap_eligible = total_items >= 5

    free_soap = None
    try:
        free_soap = Product.objects.get(name="Pendle Moor")
    except Product.DoesNotExist:
        free_soap_eligible = False

    context = {
        'free_soap_eligible': free_soap_eligible,
        'free_soap': free_soap,
    }

    return render(request, 'bag/bag.html', context)


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

    total_items = sum(bag.values())

    try:
        free_soap = Product.objects.get(name="Pendle Moor")
        soap_id = str(free_soap.id)

        if total_items >= 5 and soap_id not in bag:
            bag[soap_id] = 1
            messages.success(request, f'🎉 You qualified for a free {free_soap.name}! It has been added to your bag.')

    except Product.DoesNotExist:
        messages.warning(
            request, "The free soap offer is currently unavailable.")

    request.session['bag'] = bag
    request.session.modified = True
    return redirect(redirect_url)


def update_bag(request, item_id):
    """ Update the quantity of the specified product in the bag """

    try:
        product = Product.objects.get(pk=item_id)
        quantity = int(request.POST.get('quantity', 1))
        bag = request.session.get('bag', {})

        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id, None)
            messages.success(request, f'Added {product.name} to your bag')

        request.session['bag'] = bag
        request.session.modified = True

        return redirect('view_bag')

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def remove_from_bag(request, item_id):
    """ Remove item from the shopping bag and update free soap eligibility """

    try:
        product = Product.objects.get(pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in bag:
            del bag[item_id]
            messages.success(request, f'Removed {product.name} from your bag')

        total_items = sum(bag.values())

        try:
            free_soap = Product.objects.get(name="Pendle Moor")
            soap_id = str(free_soap.id)

            if total_items < 5 and soap_id in bag:
                del bag[soap_id]
                messages.warning(request, f'You no longer qualify for a free {free_soap.name}. It has been removed.')

        except Product.DoesNotExist:
            pass

        request.session['bag'] = bag
        request.session.modified = True

        return redirect('view_bag')

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
