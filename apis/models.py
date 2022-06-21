from django.db import models
from django.urls import reverse

# Create your models here.
class EQSecurity(models.Model):

    symbol = models.CharField( max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    series = models.CharField( max_length=3 )
    date = models.DateField(  )
    value = models.IntegerField()
    isin = models.CharField( max_length=15 )


    class Meta:
        verbose_name = "EQSecurity"
        verbose_name_plural = "EQSecurities"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("EQSecurity_detail", kwargs={"pk": self.pk})



class Bhavcopy(models.Model):

    symbol = models.OneToOneField(EQSecurity, on_delete=models.CASCADE)
    series = models.CharField( max_length=3 )
    date = models.DateField(  )
    prev_close = models.FloatField()
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    last_price = models.FloatField()
    close_price = models.FloatField()
    avg_price = models.FloatField()
    ttl_qnty = models.IntegerField()
    turnover =  models.FloatField()
    trades = models.IntegerField()
    deliv_qty = models.IntegerField()
    deliv_per = models.FloatField()

    def __str__(self):
        return self.symbol.name

    def get_absolute_url(self):
        return reverse("Bhavcopy_detail", kwargs={"pk": self.pk})
