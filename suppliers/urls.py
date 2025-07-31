from . import views
from django.urls import path

urlpatterns = [
    path('supplier/list/', views.SupplierListView.as_view(), name='supplier_list'),
    path('supplier/create/', views.SupplierCreateView.as_view(), name='supplier_create'),
    path('supplier/<int:pk>/detail/', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('supplier/<int:pk>/update/', views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('supplier/<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='supplier_delete'),

    path('api/v1/suppliers/', views.SupplierListCreateApiView.as_view(), name='suppliers_list_create_api_view'),
    path('api/v1/suppliers/<int:pk>/', views.SupplierRetrieveUpdateDestroyApiView.as_view(), name='suppliers_retrieve_update_destroy_api_view'),
]
