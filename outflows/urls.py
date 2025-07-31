from django.urls import path
from . import views, views_api


urlpatterns = [
    path('outflow/list/', views.OutflowListView.as_view(), name='outflow_list'),
    path('outflow/create/', views.OutflowCreateView.as_view(), name='outflow_create'),
    path('outflow/<int:pk>/detail/', views.OutflowDetailView.as_view(), name='outflow_detail'),

    path(
        'api/v1/outflows/',
        views_api.OutflowListCreateApiView.as_view(),
        name='outflows_list_create_api_view'
    ),
    path(
        'api/v1/outflows/<int:pk>/',
        views_api.OutflowRetrieveView.as_view(),
        name='outflows_retrieve_api_view'
    ),
]
