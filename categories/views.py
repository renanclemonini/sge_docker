from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models


class CategoryListView(LoginRequiredMixin, ListView):
    # pyrefly: ignore  # bad-override
    model = models.Category
    # pyrefly: ignore  # bad-override
    template_name = 'category_list.html'
    # pyrefly: ignore  # bad-override
    context_object_name = 'categories'
    # pyrefly: ignore  # bad-override
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class CategoryCreateView(LoginRequiredMixin, CreateView):
    # pyrefly: ignore  # bad-override
    model = models.Category
    # pyrefly: ignore  # bad-override
    template_name = 'category_create.html'
    # pyrefly: ignore  # bad-override
    form_class = forms.CategoryForm
    # pyrefly: ignore  # bad-override
    success_url = reverse_lazy('category_list')


class CategoryDetailView(LoginRequiredMixin, DetailView):
    # pyrefly: ignore  # bad-override
    model = models.Category
    # pyrefly: ignore  # bad-override
    template_name = 'category_detail.html'


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    # pyrefly: ignore  # bad-override
    model = models.Category
    # pyrefly: ignore  # bad-override
    template_name = 'category_update.html'
    # pyrefly: ignore  # bad-override
    form_class = forms.CategoryForm
    # pyrefly: ignore  # bad-override
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    # pyrefly: ignore  # bad-override
    model = models.Category
    # pyrefly: ignore  # bad-override
    template_name = 'category_delete.html'
    # pyrefly: ignore  # bad-override
    success_url = reverse_lazy('category_list')
