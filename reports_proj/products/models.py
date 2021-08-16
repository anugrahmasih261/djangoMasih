from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='products', default='no_picture.png')
    price = models.FloatField(help_text='in US dollars $')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.created.strftime('%d/%m/%Y')}"

    #{self.created.strftime('%d/%m/%Y')} this line will help to know when a product was added with date
    #and if we put code till only {self.created}" it will alsso show us the time so 'strftime' word helps to display
    # date/month/year if we remove strftime it shows the exact time product was created
