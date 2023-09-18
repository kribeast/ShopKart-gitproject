from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    category_image = models.ImageField(upload_to='categories')

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)  # Call the "real" save() method.


    class Meta:
        verbose_name_plural="Categories"


    def get_absolute_url(self):
        return reverse('product_by_category',args=[self.slug])



    def __str__(self):
        return self.category_name

class SizeVarient(BaseModel):
    size_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.size_name


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    price = models.IntegerField()
    product_description = models.TextField()
    size_varient = models.ManyToManyField(SizeVarient, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product,self).save(*args,**kwargs)


    class Meta:
        verbose_name_plural = 'products'


    def get_absolute_url(self):
        return reverse('get_product',args=[self.slug])
    

    def get_product_price_by_size(self, size):
        return self.price + SizeVarient.objects.get(size_name=size).price


    def __str__(self):
        return self.product_name
    

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to="products")