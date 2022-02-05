from django.contrib import admin
from main.models import Todo
# Register your models here


# class TodoAdmin(admin.ModelAdmin):
#     list_display = ("title", "description", "sent_at")
admin.site.register(Todo)