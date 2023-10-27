from django.db import models

class Product(models.Model):
    prod_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    owner = models.ForeignKey('auth.User', related_name='product', on_delete=models.CASCADE)