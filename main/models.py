from django.db import models
# CATEGORY_CHOICES = (
#     ('S', 'Shirt'),
#     ('SW', 'Sport wear'),
#     ('OW', 'Outwear')
# )
# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    #category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    description = models.TextField()
    #image = models.ImageField()



class OrderItem(models.Model):
    user = models.CharField(max_length=30,null = True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item,related_name="items", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    user = models.CharField(max_length=30,null = True)
    items = models.ManyToManyField(OrderItem,related_name="items")
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    


    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total

