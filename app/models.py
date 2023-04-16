from django.db import models


# Create your models here.


class info(models.Model):
    Name=models.CharField(max_length=100,blank=False,null=False)
    email=models.EmailField(max_length=100,blank=False,null=False)
    pass1=models.CharField(max_length=100,blank=False,null=False)


    def __str__(self) :
        return self.Name


class catogory(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    image=models.ImageField(upload_to='static/products',null=False,blank=False)
    description=models.TextField(max_length=300,null=False,blank=False)
    date=models.DateField()
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")

    def __str__(self) :
        return self.name
    



class products(models.Model):
    catogory=models.ForeignKey(catogory,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=False,null=False)
    #brand=models.CharField(max_length=170)
    old_price=models.IntegerField(blank=False,null=False)
    new_price=models.IntegerField(blank=False,null=False)
    ratings=models.FloatField(blank=False,null=False)
    stocks=models.IntegerField(blank=False,null=False)
    
    image=models.ImageField(upload_to='static/products',null=False,blank=False)
    description=models.TextField(max_length=300,null=False,blank=False)
    date=models.DateField()
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    

    def __str__(self) :
        return self.name
    


    
class review(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    rate=models.FloatField(blank=False,null=False)
    reviews=models.TextField(max_length=300,null=False,blank=False)
    productname=models.CharField(max_length=100,blank=False,null=False)
    pos=models.IntegerField(blank=True,null=True)
    neg=models.IntegerField(blank=True,null=True)
    neu=models.IntegerField(blank=True,null=True)
    catogory=models.CharField(max_length=100,blank=False,null=False)

    
    overall=models.CharField(max_length=100,blank=False,null=False)
    
    def __str__(self) :
        return self.name
    
    
    
    

    
    




    
    