from django.urls import path
from . import views, views_api


urlpatterns = [
    path('brands/list/', views.BrandListView.as_view(), name='brand_list'),
    path('brands/create/', views.BrandCreateView.as_view(), name='brand_create'),
    path('brands/<int:pk>/detail/', views.BrandDetailView.as_view(), name='brand_detail'),
    path('brands/<int:pk>/update/', views.BrandUpdateView.as_view(), name='brand_update'),
    path('brands/<int:pk>/delete/', views.BrandDeleteView.as_view(), name='brand_delete'),

    path('api/v1/brands/', views_api.BrandListCreateAPIView.as_view(), name='brands_create_list_api_view'),
    path(
        'api/v1/brands/<int:pk>/',
        views_api.BrandRetrieveUpdateDestoyView.as_view(),
        name='brands_retrieve_update_destroy_api_view'
    ),
]
