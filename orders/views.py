from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from cart.cart import Cart
from orders.models import OrderItem
from .forms import OrderForm

@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        order_form = OrderForm(request.POST,)

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,
                )

            cart.clear()
            
            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()

    return render(request, 'orders/order_create.html',{
        'form': order_form,
    })