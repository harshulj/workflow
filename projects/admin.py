from django.contrib import admin

from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display    = ('id', 'name', 'state', 'entry', 'created_on', 'updated_on',)
    list_filter     = ('state', 'created_on', 'updated_on',)
    search_fields   = ('name',)
    list_display_links = ('name',)


admin.site.register(Project, ProjectAdmin)
