from django.contrib import admin

from flows.models import Flow

from .models import Project

class FlowInline(admin.TabularInline):
    model   = Flow
    extra   = 0

class ProjectAdmin(admin.ModelAdmin):
    inlines         = (FlowInline,)
    list_display    = ('id', 'name', 'state', 'entry', 'created_on', 'updated_on',)
    list_filter     = ('state', 'created_on', 'updated_on',)
    search_fields   = ('name',)
    list_display_links = ('name',)


admin.site.register(Project, ProjectAdmin)
