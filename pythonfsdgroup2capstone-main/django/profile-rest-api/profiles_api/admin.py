from django.contrib import admin
from profiles_api import models

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.Book)
admin.site.register(models.Employee)
admin.site.register(models.ProfileFeedItem)
admin.site.register(models.Movie)
admin.site.register(models.Tickets)
admin.site.register(models.Movierelease)
