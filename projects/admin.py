from django.contrib import admin

from flows.models import Flow

from .models import Project, Processor

class FlowInline(admin.TabularInline):
    model   = Flow
    extra   = 0

class PreprocessorInline(admin.TabularInline):
    model   = Processor
    extra   = 0


class ProcessorAdmin(admin.ModelAdmin):
    list_display    = ('id', 'name', 'created_on', 'updated_on',)
    list_filter     = ('created_on', 'updated_on',)
    search_fields   = ('name',)
    list_display_links = ('name',)



class ProjectAdmin(admin.ModelAdmin):
    inlines         = (FlowInline,)
    list_display    = ('id', 'name', 'state', 'entry', 'created_on', 'updated_on',)
    list_filter     = ('state', 'created_on', 'updated_on',)
    search_fields   = ('name',)
    list_display_links = ('name',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Processor, ProcessorAdmin)
