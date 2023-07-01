from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created']


class Product(models.Model):
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=13)
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']


class Price(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product.name
    
    class Meta:
        ordering = ['-created']