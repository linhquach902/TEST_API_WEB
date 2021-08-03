from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.VendorListView.as_view(),name='vendor_list'),
    path('<int:pk>/', views.VendorDetailView.as_view(),name='vendor_detail'),
    path('create/', views.VendorCreateView.as_view(),name='vendor_create'), 
    path('update/<int:pk>/', views.VendorUpdateView.as_view(),name='vendor_update'), 
    path('delete/<int:pk>/', views.VendorDeleteView.as_view(),name='vendor_delete'), 
] 
