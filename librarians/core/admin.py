from django.contrib import admin

from librarians.core.models import Tags, Matter, Content


class ContentInline(admin.TabularInline):
    model = Content
    extra = 1


class MatterAdmin(admin.ModelAdmin):
    inlines = [
        ContentInline,
    ]
    list_display = ('title',)


admin.site.register(Tags)
admin.site.register(Matter, MatterAdmin)
