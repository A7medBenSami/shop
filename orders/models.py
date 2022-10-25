import decimal
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    details = models.ManyToManyField(Product,through='OrderDetails')
    is_finished = models.BooleanField()

    def __str__(self):
        return 'User : ' + self.user.username + ',Order ID : ' + str(self.id)

class OrderDetails(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return 'User : ' + self.order.user.username + 'Products : ' + self.product.name + 'Order ID : ' + str(self.order.id)

    @property
    def qtyprice(self):
        newprice =self.product.price * self.quantity
        return newprice   

    


    @property
    def qtsh(self):
        shipping = decimal.Decimal(0.05)
        totalprice =self.qtyprice + shipping
        return round(totalprice,3)  

    class Meta:
        ordering =['-id']