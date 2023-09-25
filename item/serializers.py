from rest_framework import serializers
import stripe

from item.models import Item
from config.settings import API_KEY, BASE_URL

class ItemBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        exclude = ('id', )


class ItemSerializer(serializers.ModelSerializer):
    pay_id = serializers.SerializerMethodField()
    
    class Meta:
        model = Item
        fields = ('pay_id',)


    def get_pay_id(self, item):
        stripe.api_key = API_KEY
        item_product = stripe.Product.create(name=item.name, description=item.description)
        item_price = stripe.Price.create(
            product=item_product.id,

            unit_amount_decimal=item.price * 100,
            currency="usd",
            )
        
        pay_obj = stripe.checkout.Session.create(line_items=[
                {
                    'price': item_price.id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=f'{BASE_URL}static/success.html',
            cancel_url=f'{BASE_URL}static/cancel.html',
            )

        return pay_obj.id