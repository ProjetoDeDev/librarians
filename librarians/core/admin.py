from django.contrib import admin

from librarians.core.models import Tags, Matter, Content


class ContentInline(admin.TabularInline):
    model = Content
    extra = 1


class MatterAdmin(admin.ModelAdmin):
    inlines = [
        ContentInline,
    ]
    list_display = ('title','get_tags')
    search_fields = ['tags__title', 'title']

    def get_tags(self, obj):
        return "\n- ".join([p.title for p in obj.tags.all()])

admin.site.register(Tags)
admin.site.register(Matter, MatterAdmin)
