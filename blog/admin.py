from django.contrib import admin
from . import models

class CommentSection(admin.TabularInline):
    model = models.Comment
    fields = (
        'name',
        'email',
        'text',
        'approved'
    )
    readonly_fields = (
        'name',
        'text',
        'text',
    )


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

inlines = [CommentSection]

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'approved',
        'created',
    )

    search_fields = (
        'name',
        'text',
    )

    list_filter = (
        'approved',
    )


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)
