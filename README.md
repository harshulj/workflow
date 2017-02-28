# Workflow
Workflow is an application for defining rules and flows for an entire workflow. This is just a set of instructions that needs to followed for accomplishing a bigger task. 
You can break down a big task in simple/smaller tasks and use this system to flow the data from one subtask to another.

## Design
This system is divided into projects. Each project has a different workflow that you need to define. Each project is comprised of *Flow* and *Rule*. 
### Flow
A flow is basically a subtask that needs to be implemented. A task can move from one flow to another using a set of rules.
### Rule
A Rule is a set of check that defines operation that needs to be applied on the response of previous subtask. Based on the check next workflow is selected.

## Limitations
Currently one Rule can have one check on a single key. But this can easily be changed to support multiple operations on multiple keys.

## Deployment
This is a django application hence can be deployed behind any wsgi server. Fabric can be used to automate the deployment process.
