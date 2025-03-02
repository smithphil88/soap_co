from django.shortcuts import render, redirect
from django.http import JsonResponse
# Create your views here.


def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


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
