from django.urls import path

from item.apps import ItemConfig
from item.views import ItemRetrieveAPIView, ItemHTMLAPIView, ItemCreateAPIView


app_name = ItemConfig.name


urlpatterns = [
    path('buy/<int:pk>/', ItemRetrieveAPIView.as_view(), name='buy'),
    path('item/<int:pk>/', ItemHTMLAPIView.as_view(), name='item'),
    path('item/', ItemCreateAPIView.as_view(), name='item_create'),
]