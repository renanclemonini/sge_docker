from rest_framework import generics, serializers as drf_serializers
from . import models, serializers, utils


class OutflowListCreateApiView(generics.ListCreateAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        product = validated_data['product']
        quantity = validated_data['quantity']

        if quantity <= 0:
            raise drf_serializers.ValidationError({
                'detail': 'Quantidade não pode ser menor ou igual a zero.'
            })
        elif quantity > product.quantity:
            raise drf_serializers.ValidationError({
                'detail': f'Quantidade {quantity} é maior que a quantidade disponível: {product.quantity}.'
            })
        outflow = serializer.save()
        if utils.product_decrease(outflow):
            return super().perform_create(serializer)


class OutflowRetrieveView(generics.RetrieveAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer
