
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart

# Create your views here.

@require_POST
@csrf_exempt
def add_to_cart(request, product_id):
    try:
        cart = Cart(request)
        product = get_object_or_404(Product, pk=product_id)
        cart.add(product)
        context = {
            'item_count':len(cart),
            'total_price':cart.get_total_price()
        }
        # send_sms_normal('09911660921', 'send SMS')
        return JsonResponse(context)
    except:
        return JsonResponse({'error':'Something went wrong'})
