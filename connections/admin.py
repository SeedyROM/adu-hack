from django.contrib import admin

from connections import models

admin.site.register(models.Site)
admin.site.register(models.Job)
admin.site.register(models.Service)
admin.site.register(models.Review)
