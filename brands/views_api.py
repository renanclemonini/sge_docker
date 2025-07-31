from django.db.models.deletion import ProtectedError
from rest_framework import generics, serializers as drf_serializers
from . import models, serializers


class BrandListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer


class BrandRetrieveUpdateDestoyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except ProtectedError as e:
            raise drf_serializers.ValidationError(
                {
                    'detail': f'Não é possível excluir a marca {instance.name} porque há produtos vinculados a ela',
                    'protected_objects': [str(obj) for obj in e.protected_objects]
                }
            )
