from django.contrib import admin
from .models import (Contact, Ad ,Category)
# Register your models here.

admin.site.register(Contact)
admin.site.register(Ad)
admin.site.register(Category)