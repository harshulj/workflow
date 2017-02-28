from django.contrib import admin

from .models import Flow, Rule


class RuleInline(admin.TabularInline):
    model   = Rule
    fk_name = 'flow'
    extra   = 0


class FlowAdmin(admin.ModelAdmin):
    inlines         = (RuleInline,)
    list_display    = ('name', 'type', 'project', 'created_on', 'updated_on',)
    list_filter     = ('type', 'created_on', 'updated_on',)
    search_fields   = ('name',)
    list_display_links = ('name',)


class RuleAdmin(admin.ModelAdmin):
    list_display    = ('__unicode__', 'flow', 'next_flow', 'key', 'operation', 'created_on', 'updated_on',)
    list_filter     = ('operation', 'created_on', 'updated_on',)
    search_fields   = ('flow', 'next_flow',)
    #list_display_links = ('name',)



admin.site.register(Flow, FlowAdmin)
admin.site.register(Rule, RuleAdmin)
