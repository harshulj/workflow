from __future__ import unicode_literals

from django.db import models

from flows.models import Flow

from .constants import ProjectStates

class Project(models.Model):
    '''
    This represents a single project. Each project can have multiple flows.
    with multiple nesting. The outcome of each flow will define the next
    flow that needs to be executed for a particular task.
    '''
    name        = models.CharField(max_length=128)
    entry       = models.ForeignKey(Flow, blank=True, null=True, related_name='entry_for')
    state       = models.CharField(max_length=3,
            choices=ProjectStates.choices(), default=ProjectStates.NEW)
    processors  = models.ManyToManyField('Processor', related_name='projects')

    created_on  = models.DateTimeField(auto_now_add=True)
    updated_on  = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Processor(models.Model):
    name    = models.CharField(max_length=128)

    created_on  = models.DateTimeField(auto_now_add=True)
    updated_on  = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.name
