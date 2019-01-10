from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Order(models.Model):
    orderNum = models.AutoField('ORDERNUM',primary_key=True)
    eventName = models.CharField('EVENTNUM',max_length = 50, allow_unicode=True,help_text=
    'Input word for Event name')
    material = models.CharField('MATERAIL', max_length = 50)
    color = models.CharField('COLOR', max_length = 50)
    size = models.CharField('SIZE', max_length = 50)
    amount = models.IntegerFiled('AMOUNT')
    deadLine = models.DateTimeField('DEAD LINE')
    price = models.IntegerField('PRICE')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        db_table = 'my_order'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.orderNum
