from rest_framework import generics, serializers as drf_serializers
from . import models, serializers, utils


class InflowListCreateApiView(generics.ListCreateAPIView):
    queryset = models.Inflow.objects.all()
    serializer_class = serializers.InflowsSerializer

    def perform_create(self, serializer):
        inflow: models.Inflow = serializer.save()
        if inflow.quantity <= 0:
            raise drf_serializers.ValidationError(
                {
                    'detail': 'Quantidade deve ser maior que zero.'
                }
            )
        if utils.product_increase(inflow):
            return super().perform_create(serializer)


class InflowRetrieveApiView(generics.RetrieveAPIView):
    queryset = models.Inflow.objects.all()
    serializer_class = serializers.InflowsSerializer
