from django.db import models


# Create your models here.
class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Pizza name')
    description = models.TextField(verbose_name="descriptions")
    rating = models.FloatField(default=0, verbose_name='Rating')
    url = models.URLField(verbose_name='Internet-address Pizza')

    class Meta:
        verbose_name = "Pizzaplace"
        verbose_name_plural = 'PizzaPlaces'
    #     ordering = ['price']

    def __str__(self):
        return self.name


class Pizza(models.Model):
    PizzaShop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Name of Pizza')
    short_descriptions = models.CharField(max_length=30, verbose_name="short description")
    price = models.IntegerField(default=0, verbose_name='Price')

    def __str__(self):
        return self.name
