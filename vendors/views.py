from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Vendor

class VendorListView(ListView):
    model = Vendor
    template_name = 'vendors/vendor_list.html'
    context_object_name = 'list_all_vendor' 

    def get_queryset(self):
        vendor_ID = self.request.GET.get('vendor_ID', None)
        if vendor_ID:
            qs = Vendor.objects.filter(vendor_ID=vendor_ID)
            return qs
        return super().get_queryset()

class VendorDetailView(DetailView):
    model = Vendor
    template_name = 'vendors/vendor_detail.html'
    context_object_name = 'vendor' 

class VendorCreateView(CreateView):
    model = Vendor
    template_name = 'vendors/vendor_create.html'
    fields = '__all__'
    success_url = reverse_lazy('vendor_create')

class VendorUpdateView(UpdateView):
    model = Vendor
    template_name = 'vendors/vendor_update.html'
    fields = '__all__'

class VendorDeleteView(DeleteView):
    model = Vendor
    template_name = 'vendors/vendor_delete.html'
    context_object_name = 'vendor' 
    success_url = reverse_lazy('vendor_list')