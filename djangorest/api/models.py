from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    address3 = models.CharField(max_length=255, blank=True)
    postnr = models.IntegerField(blank=True)
    poststed = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=64, blank=True)
    webpage = models.URLField(max_length=64, blank=True)
    def __str__(self):
        return "{}".format(self.name)

class Order(models.Model):
    order_date = models.DateField(blank=False) 
    ship_date = models.DateField(blank=True) 
    total_cost = models.IntegerField(blank=True)
    paid_date = models.DateField(blank=True) 
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.order_date)

class OrderLine(models.Model):
    product = models.CharField(max_length=30, blank=True)
    quantity = models.IntegerField(blank=True)
    unit = models.CharField(max_length=30, blank=True)
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.product)