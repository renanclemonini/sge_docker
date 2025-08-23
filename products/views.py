from rest_framework import generics, serializers as drf_serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.deletion import ProtectedError
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import forms, models, serializers
from brands.models import Brand
from categories.models import Category
from app import metrics


class ProductListView(LoginRequiredMixin, ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        context['categories'] = Category.objects.all()
        context['product_metrics'] = metrics.get_product_metrics()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        serie_number = self.request.GET.get('serie_number')
        brand_id = self.request.GET.get('brand')
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        if brand_id:
            queryset = queryset.filter(brand__id=brand_id)
        if title:
            queryset = queryset.filter(title__icontains=title)
        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)

        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = models.Product
    template_name = 'product_detail.html'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Product
    template_name = 'product_update.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')


class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except ProtectedError as e:
            raise drf_serializers.ValidationError(
                {
                    'detail': f'Não é possível excluir o produto {str(instance)} porque há elementos vinculados',
                    'protected_objects': [str(obj) for obj in e.protected_objects]
                }
            )
