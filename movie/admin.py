from django.contrib import admin
from .models import Emails,Movie,Review
# Register your models here.
admin.site.register(Emails)
admin.site.register(Movie)
admin.site.register(Review)