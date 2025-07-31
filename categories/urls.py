from django.urls import path
from . import views, views_api

urlpatterns = [
    path('categories/list/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path(
        'api/v1/categories/',
        views_api.CategoryListCreateApiView.as_view(),
        name='list_create_categories_api_view'
    ),
    path(
        'api/v1/categories/<int:pk>/',
        views_api.CategoryRetrieveUpdateDestroyApiView.as_view(),
        name='list_create_categories_api_view'
    ),
]
