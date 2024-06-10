from django.contrib import admin
from .models import User, Propiedad, SolicitudArriendo, Region, Comuna
# Register your models here.

admin.site.register(User)
admin.site.register(Propiedad)
admin.site.register(SolicitudArriendo)
admin.site.register(Region)
admin.site.register(Comuna)
