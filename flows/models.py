from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


from .constants import FlowTypes, RuleOperations


class Flow(models.Model):
    '''
    A flow defines the settings and flow for categorization tasks.
    '''
    name        = models.CharField(max_length=128)
    type        = models.CharField(max_length=3, choices=FlowTypes.choices())
    project     = models.ForeignKey('projects.Project', related_name='flows')
    settings    = JSONField(default={})

    created_on  = models.DateTimeField(auto_now_add=True)
    updated_on  = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Rule(models.Model):
    '''
    A rule defines the relation between two flows within a single project.
    '''
    flow            = models.ForeignKey(Flow, related_name='rules')
    next_flow       = models.ForeignKey(Flow, blank=True, null=True)

    key             = models.CharField(max_length=128)
    operation       = models.CharField(max_length=3, choices=RuleOperations.choices())
    value           = models.CharField(max_length=128)


    created_on  = models.DateTimeField(auto_now_add=True)
    updated_on  = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s to %s' % (self.flow, self.next_flow)
