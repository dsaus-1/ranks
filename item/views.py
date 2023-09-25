from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from item.models import Item
from item.serializers import ItemSerializer, ItemBaseSerializer
from config.settings import API_KEY_PUBLIC, BASE_URL


class ItemRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemHTMLAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item/item_buy.html'

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        return Response({'item': item, 'published_key': API_KEY_PUBLIC, 'url': BASE_URL})


class ItemCreateAPIView(generics.CreateAPIView):
    serializer_class = ItemBaseSerializer
    queryset = Item.objects.all()