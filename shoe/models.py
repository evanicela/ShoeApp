from django.db import models


# Create your models here.
class Shoe(models.Model):
    shoe_name = models.CharField(max_length=100)
    shoe_image = models.ImageField(null=True, blank=True, upload_to="images/")
    shoe_price = models.CharField(max_length=100)
    shoe_description = models.CharField(max_length=15)

    class Meta:
        db_table = "shoe"


class Checkout(models.Model):
    transactionid = models.CharField(db_column='transactionid', max_length=100, blank=False)
    amount = models.CharField(db_column='amount', max_length=100, blank=False)
    phone = models.CharField(db_column='phone', max_length=100, blank=False)

    class Meta:
        db_table = 'checkout'
        verbose_name = 'checkout'
        verbose_name_plural = 'checkouts'

    def __unicode__(self):
        return self.transactionid

    def __str__(self):
        return self.transactionid