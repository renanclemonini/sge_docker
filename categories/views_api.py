from django.db.models.deletion import ProtectedError
from rest_framework import generics, serializers as drf_serializers
from . import models, serializers


class CategoryListCreateApiView(generics.ListCreateAPIView):
    # pyrefly: ignore  # missing-attribute
    queryset = models.Category.objects.all()
    # pyrefly: ignore  # bad-override
    serializer_class = serializers.CategorySerializer


class CategoryRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    # pyrefly: ignore  # missing-attribute
    queryset = models.Category.objects.all()
    # pyrefly: ignore  # bad-override
    serializer_class = serializers.CategorySerializer

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except ProtectedError as e:
            raise drf_serializers.ValidationError(
                {
                    'detail': f'Não é possível excluir a categoria {instance.name} porque há produtos vinculados a ela',
                    'protected_objects': [str(obj) for obj in e.protected_objects]
                }
            )
