from django.db import models

# Create your models here.
class Account(models.Model):
    name= models.CharField( max_length=50,null=True,blank=True,db_index=True)
    Transaction_Type= models.CharField( max_length=50,null=True,blank=True,db_index=True)
    DebitAmount= models.IntegerField(null=True,blank=True,db_index=True)
    CreditAmount= models.IntegerField(null=True,blank=True,db_index=True)
    
    def __str__(self):
        return self.name


# class Transasction ():
