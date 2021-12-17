from django.contrib import admin
from home.models import Contact  
from home.models import Packages
# from home.models import User
# Register your models here.
admin.site.register(Contact)
admin.site.register(Packages)
# admin.site.register(User)