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

    # Store messages to avoid duplicates
    message_list = []

    # Add/update product quantity in bag
    if item_id in bag:
        bag[item_id] += quantity
        message_list.append(f'Updated {product.name} quantity')
    else:
        bag[item_id] = quantity
        message_list.append(f'Added {product.name} to your bag')

    # Calculate total items excluding the free soap
    total_items = sum(
        qty for key, qty in bag.items() if Product.objects.get(pk=key).name != "Pendle Moor (Free)")

    try:
        free_soap = Product.objects.get(name="Pendle Moor (Free)")
        soap_id = str(free_soap.id)

        if total_items >= 5 and soap_id not in bag:
            bag[soap_id] = 1
            message_list.append(f'🎉 You qualified for a free {free_soap.name}! It has been added to your bag.')

        elif total_items < 5 and soap_id in bag:
            del bag[soap_id]
            message_list.append(f'You no longer qualify for a free {free_soap.name}. It has been removed.')

    except Product.DoesNotExist:
        pass  # No free product exists

    request.session['bag'] = bag
    request.session.modified = True

    # Add all messages at once
    messages.success(request, " ".join(message_list))

    return redirect(redirect_url)


def update_bag(request, item_id):
    """ Update the quantity of the specified product in the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    message_list = []  # Store messages to avoid duplicates

    if quantity > 0:
        bag[item_id] = quantity
        message_list.append(f'Updated {product.name} quantity to {quantity}')
    else:
        bag.pop(item_id, None)
        message_list.append(f'Removed {product.name} from your bag')

    # Recalculate total items excluding the free soap
    total_items = sum(qty for key, qty in bag.items() if Product.objects.get(pk=key).name != "Pendle Moor (Free)")

    try:
        free_soap = Product.objects.get(name="Pendle Moor (Free)")
        soap_id = str(free_soap.id)

        # Check if user qualifies for the free soap
        if total_items >= 5:
            if soap_id not in bag:  # Only show message if it's a new addition
                bag[soap_id] = 1
                message_list.append(f'🎉 You qualified for a free {free_soap.name}! It has been added to your bag.')

        # Remove free soap if total items drop below 5
        elif total_items < 5 and soap_id in bag:
            del bag[soap_id]
            message_list.append(f'You no longer qualify for a free {free_soap.name}. It has been removed.')

    except Product.DoesNotExist:
        pass  # Free soap does not exist

    request.session['bag'] = bag
    request.session.modified = True

    # Add all messages at once
    if message_list:
        messages.success(request, " ".join(message_list))

    return redirect('view_bag')


def remove_from_bag(request, item_id):
    """ Remove item from the shopping bag and update free soap eligibility """

    try:
        product = Product.objects.get(pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in bag:
            del bag[item_id]
            messages.success(request, f'Removed {product.name} from your bag')

        # Recalculate total items excluding the free soap
        total_items = sum(
            qty for key,
            qty in bag.items() if Product.objects.get(pk=key).name !=
            "Pendle Moor (Free)")

        try:
            free_soap = Product.objects.get(name="Pendle Moor (Free)")
            soap_id = str(free_soap.id)

            # Remove the free soap if the total falls below 5
            if total_items < 5 and soap_id in bag:
                del bag[soap_id]
                messages.warning(
                    request,
                    f"You no longer qualify for a free {free_soap.name}. "
                    "It has been removed."
                )
        except Product.DoesNotExist:
            pass

        request.session['bag'] = bag
        request.session.modified = True

        return redirect('view_bag')

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
