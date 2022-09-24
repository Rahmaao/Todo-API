from xml.dom import ValidationErr
from django.shortcuts import render
from rest_framework import generics
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Item
from list import serializers

# Create your views here.

class TodoList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def delete(self, request, *args, **kwargs):
        item = Item.objects.filter(pk=kwargs['pk'])
        if item.exists():
            return self.destroy(request, *args, **kwargs)
        # else:
        #     return
            # raise ValidationError('This item doesn\'t exist')

    def update(self, request, *args, **kwargs):
        item = Item.objects.filter(pk=kwargs['pk']).first()
        if item:
            serializer = ItemSerializer(item, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

        # else:
        #     raise ValidationError('You cannot update this post')
