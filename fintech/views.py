import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY


def buy_item(request, id):
    item = get_object_or_404(Item, id=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://davewalker.ru/success/',
        cancel_url='https://davewalker.ru/cancel/',
    )
    return JsonResponse({'session_id': session.id})


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    context = {
        'item': item,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'item_detail.html', context)


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.calculate_total()
    discounts = order.discount_set.all()
    taxes = order.tax_set.all()
    context = {
        'order': order,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'discounts': discounts,
        'taxes': taxes,
    }
    return render(request, 'order_detail.html', context)


def create_payment_intent(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.calculate_total()
    payment_intent = stripe.PaymentIntent.create(
        amount=int(order.total_amount * 100),
        currency=order.items.first().currency,
    )

    return JsonResponse({
        'clientSecret': payment_intent['client_secret']
    })


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')


def home(request):
    return render(request, 'home.html')