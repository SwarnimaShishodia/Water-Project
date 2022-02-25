from django.db import models

class Supplier(models.Model):
    email=models.CharField(max_length=50,primary_key=True)
    comname=models.CharField(max_length=150)
    comowner=models.CharField(max_length=50)
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.IntegerField()
    shoplicense= models.ImageField(upload_to='shoplicense/',null=True,blank=True)
    fssai= models.ImageField(upload_to='fssai/',null=True,blank=True)
    gsti_pan= models.ImageField(upload_to='gsti_pan/',null=True,blank=True)

    def __str__(self):
        return self.comname