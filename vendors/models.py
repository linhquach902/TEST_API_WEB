from django.db import models
from django.urls import reverse

# Create your models here.
class Vendor(models.Model):
    company_name = models.CharField(max_length=200)
    vendor_ID = models.CharField(max_length=50)
    point_contact_name = models.CharField(max_length=200)
    vendor_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    vendor_email = models.CharField(max_length=100)
    company_type = models.CharField(max_length=200)
    accept_card = models.CharField(max_length=50,null=True)

    def get_absolute_url (self):
        return reverse('vendor_detail', args=[str(self.id)])