from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from app import metrics
from . import forms, models, utils


class OutflowListView(LoginRequiredMixin, ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')
        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['sales_metrics'] = metrics.get_sales_metrics()

        return context_data


class OutflowCreateView(LoginRequiredMixin, CreateView):
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')

    def form_valid(self, form):
        if form.cleaned_data.get('quantity', 0) <= 0:
            form.add_error('quantity', 'A quantidade não pode ser menor ou igual a zero.')
            return self.form_invalid(form)
        outflow: models.Outflow = form.save(commit=False)
        outflow.save()
        if utils.product_decrease(outflow):
            utils.send_outflow_event(outflow)
            return super().form_valid(form)


class OutflowDetailView(LoginRequiredMixin, DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'
