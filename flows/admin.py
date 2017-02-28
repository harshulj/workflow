from django.contrib import admin

from .models import Flow, Rule

class FlowAdmin(admin.ModelAdmin):
    pass

class RuleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Flow, FlowAdmin)
admin.site.register(Rule, RuleAdmin)
