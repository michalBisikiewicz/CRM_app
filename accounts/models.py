from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=155, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Promocja', 'Promocja'),
    )
    name = models.CharField(max_length=150, null=True)
    price = models.FloatField(max_length=150, null=True)
    category = models.CharField(max_length=150, null=True, choices=CATEGORY)
    description = models.TextField(max_length=150, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Oczekuje', 'Oczekuje'),
        ('W drodze', 'W drodze'),
        ('Dostarczone', 'Dostarczone'),

    )
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=150, null=True,choices=STATUS)

    def __str__(self):
        return self.name