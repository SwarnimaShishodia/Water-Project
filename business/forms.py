from django import forms
#from django.contrib.auth.models import User
from business.models import Supplier

class Company(forms.ModelForm):
    class Meta:
        model=Supplier
        fields=['email','comname','comowner','address','city','state','pincode','shoplicense','fssai','gsti_pan']
