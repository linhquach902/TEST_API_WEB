from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import OrderPlan

class OrderPlanListView(ListView):
    model = OrderPlan
    template_name = 'orderPlan/orderPlan_list.html'
    context_object_name = 'list_all_orderPlan' 

    def get_queryset(self):
        code = self.request.GET.get('code', None)
        if code:
            qs = OrderPlan.objects.filter(code=code)
            return qs
        return super().get_queryset()

class OrderPlanDetailView(DetailView):
    model = OrderPlan
    template_name = 'orderPlan/orderPlan_detail.html'
    context_object_name = 'orderPlan' 

class OrderPlanCreateView(CreateView):
    model = OrderPlan
    template_name = 'orderPlan/orderPlan_create.html'
    fields = '__all__'
    success_url = reverse_lazy('orderPlan_create')

class OrderPlanUpdateView(UpdateView):
    model = OrderPlan
    template_name = 'orderPlan/orderPlan_update.html'
    fields = '__all__'

class OrderPlanDeleteView(DeleteView):
    model = OrderPlan
    template_name = 'orderPlan/orderPlan_delete.html'
    context_object_name = 'orderPlan' 
    success_url = reverse_lazy('orderPlan_list')