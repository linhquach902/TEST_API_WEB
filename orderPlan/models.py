from django.db import models
from django.urls import reverse

# Create your models here.

class OrderPlan(models.Model):
    material_code = models.CharField(max_length=80, null=True)
    material_name = models.CharField(max_length=80)
    maker = models.CharField(max_length=80)
    quantity = models.IntegerField()
    buying_price = models.IntegerField()
    selling_price = models.IntegerField()
    status = models.CharField(max_length=80)

    def get_absolute_url (self):
        return reverse('orderPlan_detail', args=[str(self.id)])