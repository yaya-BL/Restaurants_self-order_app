from django.db import models
from django.conf import settings
from v1.shop.models import Shop, ShopBranch

# Food Category model
class Category(models.Model):
  branch = models.ForeignKey(ShopBranch, on_delete=models.CASCADE, blank=True, null=True)
  name = models.CharField(max_length=255)
  
  class Meta:
    verbose_name_plural='Categories'
    
  def __str__(self):
    return self.name

# Food Item model
class Item(models.Model):
  shop = models.ForeignKey(Shop, related_name="item",blank=True, null=True, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, related_name="item",blank=True, null=True, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="item",blank=True, null=True, on_delete=models.CASCADE)
  
  name = models.CharField(max_length=255)
  price = models.FloatField()
  description = models.TextField()
  image = models.ImageField(upload_to='uploads/', blank=True, null=True)
  date_added = models.DateTimeField(auto_now_add=True)
  prepare_time = models.IntegerField(default = 0)
  
  class Meta:
    ordering = ('-date_added',)
    
  def __str__(self):
    return self.name

# Order Cart model
class Cart(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='cart', on_delete=models.CASCADE)
  date_added = models.DateTimeField(auto_now_add=True)
  item = models.ManyToManyField(Item, related_name="cartItemsTest")

  def __str__(self):
    return self.user.username

# Order Cart Item model
class CartItem(models.Model):
  cart = models.ForeignKey(Cart, related_name="cartItems", on_delete=models.CASCADE)
  item = models.ForeignKey(Item, related_name="cartItems", on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural='Cart Items'

  def __str__(self):
    return self.item.name