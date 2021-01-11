from django.db import models
from django.contrib.auth.models import User
from v1.shop.models import Shop

# Food Category model
class Category(models.Model):
  user = models.ForeignKey(User, related_name="category", blank=True, null=True, on_delete=models.CASCADE)
  shop = models.ForeignKey(Shop, related_name="category", blank=True, null=True, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  
  class Meta:
    verbose_name_plural='Categories'
    
  def __str__(self):
    return self.name

# Food Item model
class Item(models.Model):

  shop = models.ForeignKey(Shop, related_name="item",blank=True, null=True, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, related_name="item",blank=True, null=True, on_delete=models.CASCADE)
  user = models.ForeignKey(User, related_name="item",blank=True, null=True, on_delete=models.CASCADE)
  
  name = models.CharField(max_length=255)
  price = models.FloatField()
  description = models.TextField(blank=True, null=True)
  image = models.ImageField(upload_to='uploads/', blank=True, null=True)
  date_added = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ('-date_added',)
    
  def __str__(self):
    return self.name

# Order Cart model
class Cart(models.Model):
  user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user.username

# Order Cart Item model
class CartItems(models.Model):
  cart = models.ForeignKey(Cart, related_name="cartItems", on_delete=models.CASCADE)
  item = models.ForeignKey(Item, related_name="cartItems", on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural='Cart Items'

  def __str__(self):
    return self.item.name