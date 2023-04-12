from django.contrib import admin
from .models import ClassRoom, BucketItems, Posts
# Register your models here.
admin.site.register(ClassRoom)
admin.site.register(Posts)
admin.site.register(BucketItems)