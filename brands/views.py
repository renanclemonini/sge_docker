from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models


class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    View to list all brands.
    """
    # pyrefly: ignore  # bad-override
    model = models.Brand
    # pyrefly: ignore  # bad-override
    template_name = 'brand_list.html'
    # pyrefly: ignore  # bad-override
    context_object_name = 'brands'
    # pyrefly: ignore  # bad-override
    paginate_by = 10
    # pyrefly: ignore  # bad-override
    permission_required = 'brands.view_brand'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    View to create a new brand.
    """
    # pyrefly: ignore  # bad-override
    model = models.Brand
    # pyrefly: ignore  # bad-override
    template_name = 'brand_create.html'
    # pyrefly: ignore  # bad-override
    form_class = forms.BrandForm
    # pyrefly: ignore  # bad-override
    success_url = reverse_lazy('brand_list')
    # pyrefly: ignore  # bad-override
    permission_required = 'brands.add_brand'


class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """
    View to display the details of a specific brand.
    """
    # pyrefly: ignore  # bad-override
    model = models.Brand
    # pyrefly: ignore  # bad-override
    template_name = 'brand_detail.html'
    # pyrefly: ignore  # bad-override
    permission_required = 'brands.view_brand'


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    View to update an existing brand.
    """
    # pyrefly: ignore  # bad-override
    model = models.Brand
    # pyrefly: ignore  # bad-override
    template_name = 'brand_update.html'
    # pyrefly: ignore  # bad-override
    form_class = forms.BrandForm
    # pyrefly: ignore  # bad-override
    success_url = reverse_lazy('brand_list')
    # pyrefly: ignore  # bad-override
    permission_required = 'brands.change_brand'


class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    View to delete a specific brand.
    """
    # pyrefly: ignore  # bad-override
    model = models.Brand
    # pyrefly: ignore  # bad-override
    template_name = 'brand_delete.html'
    # pyrefly: ignore  # bad-override
    success_url = reverse_lazy('brand_list')
    # pyrefly: ignore  # bad-override
    permission_required = 'brands.delete_brand'
