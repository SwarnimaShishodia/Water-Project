from django.contrib import admin
from . models import Plan
from . models import Subscribe
from . models import Reviews
from . models import Feedback
# Register your models here.
admin.site.register(Plan)
admin.site.register(Subscribe)
admin.site.register(Reviews)
admin.site.register(Feedback)
