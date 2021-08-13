from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.OrderPlanListView.as_view(),name='orderPlan_list'),
    path('<int:pk>/', views.OrderPlanDetailView.as_view(),name='orderPlan_detail'),
    path('create/', views.OrderPlanCreateView.as_view(),name='orderPlan_create'), 
    path('update/<int:pk>/', views.OrderPlanUpdateView.as_view(),name='orderPlan_update'), 
    path('delete/<int:pk>/', views.OrderPlanDeleteView.as_view(),name='orderPlan_delete'), 
] 
