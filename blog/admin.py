from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'created',
        'updated',
    )

    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )

    list_filter = (
        'status',
    )

    prepopulated_fields = {'slug': ('title', )}


# Register your models here.
admin.site.register(models.Post, PostAdmin)

# Register your models here.
