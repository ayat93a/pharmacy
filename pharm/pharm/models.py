import datetime
from time import timezone
from django.db import models
from django.contrib.auth import get_user_model 


class Product(models.Model):
    product_name = models.TextField(null='prevorder')
    days_to_supply = models.PositiveIntegerField(default=10 , null=False , blank=False )
    last_order_quantity = models.PositiveIntegerField(null=False , blank=False , default=None)
    available_quantity = models.PositiveIntegerField(default=10 , null=False , blank=False )
    cost_per_item = models.PositiveIntegerField(null=False , blank=False , default=None)
    price_per_item = models.PositiveIntegerField(null=False , blank=False , default=None)
    discount =  models.DecimalField(max_digits=2, decimal_places=1 , default=None)
    bonus = models.DecimalField(max_digits=2, decimal_places=1, default=None)
    Date = models.DateTimeField(auto_now_add=True )


    @property
    def bonus_quantity(self):
        return int(self.bonus * self.last_order_quantity)

    @property
    def total_cost(self):
        return self.cost_per_item * self.last_order_quantity

    @property
    def  total_price(self):
        return self.price_per_item* self.last_order_quantity

    @property
    def  profit_per_item (self):
        return self.price_per_item - self.cost_per_item - self.discount * self.price_per_item

    @property
    def  total_profit (self):
        return self.total_price-self.total_cost + self.bonus_quantity*self.total_price - self.discount*self.last_order_quantity*self.total_price


    
    # def save(self, *args, **kwargs):
    #     self.bonus_quantity = self.bonus_quantity
    #     self.total_cost = self.total_cost
    #     self.total_price = self.total_price
    #     self.profit_per_item = self.profit_per_item 
    #     self.total_profit = self.total_profit 
    #     super(Product,self).save()

    def __str__ (self, *args, **kwargs):
        return self.product_name

        
# class Product(models.Model):
#     drugName = models.TextField(max_length=255 , null= False , blank= False)
#     drugCost= models.PositiveIntegerField(default=0 , null=False , blank= False)
#     isThereADiscount = models.BooleanField(default= False)


#     def Discount(self):
#         if self.isThereADiscount == True :
#             discount = models.IntegerField(default=0 , null=False , blank= False)
#             cost_after_discount = self.drugCost*discount
#             # self.drugCost = cost_after_discount

#             return discount ,cost_after_discount
    

#     def totalQuantityInStock (self):
#         pass

#     def __str__(self):
#         return self.drugName

# class RequestProduct(models.Model):
#     order = models.BooleanField(default=False )
#     available_Quantity = models.PositiveIntegerField(default=0 , null=False , blank= False)

#     def generateOrder(self):
#         if self.order == True:
#             drugName = models.ForeignKey(Product , on_delete= models.CASCADE )
#             quantity = models.PositiveBigIntegerField(default=0 , null=False) 
#             orderDate = models.DateTimeField(auto_now=True)
#             request_by = models.ForeignKey(get_user_model() , on_delete=models.CASCADE  )

#         return drugName , quantity ,orderDate, request_by
