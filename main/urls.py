from django.urls import path
from .views import CarListView, BrandListView, OwnerListView

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car-list'),
    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('owners/', OwnerListView.as_view(), name='owner-list'),
]
