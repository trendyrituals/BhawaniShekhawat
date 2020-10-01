from django.contrib import admin
from .models import Service,Training,Profile,Contact,Link,ProfileImg,DevServe,Consult
# Register your models here.
admin.site.register(Profile)
admin.site.register(Service)
admin.site.register(Training)
admin.site.register(Contact)
admin.site.register(Link)
admin.site.register(ProfileImg)
admin.site.register(DevServe)
admin.site.register(Consult)