from django.db import models

# Create your models here.
class Global_Indices(models.Model):
    Name = models.CharField(max_length=200)
    Currrent_value = models.FloatField(default=0)
    change = models.FloatField(default=0)
    Per_change = models.FloatField(default=0)
    Open =  models.FloatField(default=0)
    High = models.FloatField(default=0)
    Low = models.FloatField(default=0)
    pre_close = models.FloatField(default=0)



class MAS_BSE(models.Model):
    Company_name = models.CharField(max_length=200)
    Group = models.CharField(max_length=2)
    High = models.FloatField(default=0)
    Low = models.FloatField(default=0)
    Last_Price = models.FloatField(default=0)
    Per_change = models.FloatField(default=0)
    Values_in_RS =  models.FloatField(default=0)
   

class MAS_NSE(models.Model):
    Company_name = models.CharField(max_length=200)
    High = models.FloatField(default=0)
    Low = models.FloatField(default=0)
    Last_Price = models.FloatField(default=0)
    Per_change = models.FloatField(default=0)
    Values_in_RS =  models.FloatField(default=0)

class FD_CASH(models.Model):
    F_date = models.DateField()
    F_gross_purchase = models.FloatField(default=0)
    F_gross_sales = models.FloatField(default=0)
    F_net_purchase_orsale = models.FloatField(default=0)
    D_gross_purchase = models.FloatField(default=0)
    D_gross_sales = models.FloatField(default=0)
    D_net_purchase_orsale = models.FloatField(default=0)

class FD_FII(models.Model):
    E_date = models.DateField()
    E_gross_purchase = models.FloatField(default=0)
    E_gross_sales = models.FloatField(default=0)
    E_net_purchase_orsale = models.FloatField(default=0)
    DE_gross_purchase = models.FloatField(default=0)
    DE_gross_sales = models.FloatField(default=0)
    DE_net_purchase_orsale = models.FloatField(default=0)


class FD_FandO(models.Model):
    E_date = models.DateField()
    E_gross_purchase = models.FloatField(default=0)
    E_gross_sales = models.FloatField(default=0)
    E_net_purchase_orsale = models.FloatField(default=0)
    DE_gross_purchase = models.FloatField(default=0)
    DE_gross_sales = models.FloatField(default=0)
    DE_net_purchase_orsale = models.FloatField(default=0)

class FD_MF_SEBI(models.Model):
    E_date = models.DateField()
    E_gross_purchase = models.FloatField(default=0)
    E_gross_sales = models.FloatField(default=0)
    E_net_purchase_orsale = models.FloatField(default=0)
    DE_gross_purchase = models.FloatField(default=0)
    DE_gross_sales = models.FloatField(default=0)
    DE_net_purchase_orsale = models.FloatField(default=0)



class Indian_Indices(models.Model):
    Name = models.CharField(max_length=200)
    Currrent_value = models.FloatField(default=0)
    change = models.FloatField(default=0)
    Per_change = models.FloatField(default=0)
    Open =  models.FloatField(default=0)
    High = models.FloatField(default=0)
    Low = models.FloatField(default=0)

class graph(models.Model):
    price = models.FloatField(default=0)
    year = models.IntegerField(default=0)