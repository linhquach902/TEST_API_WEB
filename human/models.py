from django.db import models
from django.urls import reverse

# Create your models here.

class Human(models.Model):
    CMND = models.CharField(max_length=50)
    ten = models.CharField(max_length=50)
    ngay_sinh = models.DateField()
    gioi_tinh = models.CharField(max_length=50,null=True)
    dia_chi = models.CharField(max_length=100,null=True)
    loai_vac_xin = models.CharField(max_length=50)
    ngay_tiem = models.DateField()
    so_lan_tiem = models.IntegerField()

    def get_absolute_url (self):
        return reverse('human_detail', args=[str(self.id)])