from django.urls import path
from . import views, views_api


urlpatterns = [
    path('inflows/list/', views.InflowListView.as_view(), name='inflow_list'),
    path('inflows/create/', views.InflowCreateView.as_view(), name='inflow_create'),
    path('inflows/<int:pk>/detail/', views.InflowDetailView.as_view(), name='inflow_detail'),

    path(
        'api/v1/inflows/',
        views_api.InflowListCreateApiView.as_view(),
        name='inflow_list_create_api_view'
    ),
    path(
        'api/v1/inflows/<int:pk>/',
        views_api.InflowRetrieveApiView.as_view(),
        name='inflow_retrieve_api_view'
    ),
]
