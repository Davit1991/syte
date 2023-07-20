from django.db import models

# Create your models here.

class IndexCaruselActive(models.Model):
    title = models.CharField('Carusel Title', max_length=60)
    name = models.CharField('Carusel name', max_length=60)
    abaut = models.TextField('Carusel abaut')
    button_name = models.CharField('Carusel button name', max_length=30)
    img = models.ImageField('Carusel image', upload_to='index_images')
    logo = models.ImageField('Carusel logo', upload_to='index_images')


    def __str__(self):
        return self.title
    

    
class IndexCarusel(models.Model):
    title = models.CharField('Carusel Title', max_length=60)
    name = models.CharField('Carusel name', max_length=60)
    abaut = models.TextField('Carusel abaut')
    button_name = models.CharField('Carusel button name', max_length=30)
    img = models.ImageField('Carusel image', upload_to='index_images')
    logo = models.ImageField('Carusel logo', upload_to='index_images')



    def __str__(self):
        return self.title


class Category(models.Model):

    name = models.CharField('Category name', max_length=60)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"


class Brand(models.Model):

       category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_brand')   
       name = models.CharField('Brand name', max_length=60)

       def __str__(self):
           return self.name        


class Product(models.Model):

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name= 'brand_prod')
    name = models.CharField('Product name', max_length=60)
    price = models.PositiveIntegerField('Product price')
    logo = models.ImageField('Product logo', blank=True)
    img = models.ImageField('Product img', blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):

    name = models.CharField('Contact name', max_length=60)
    email = models.EmailField('Contact email')
    subject = models.CharField('Contact subject', max_length=100)
    message  = models.TextField('Contact message')

    def __str__(self):
        return self.name

class Cart(models.Model):

    prod = models.ForeignKey(Product, on_delete=models.CASCADE)