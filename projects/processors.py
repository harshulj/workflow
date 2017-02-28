class Processor():
    '''
    Use this as a base class for all the processors.
    This may not be useful now but it can be used to automate the
    creation and running of processors on a task.
    '''
    def execute(self):
        raise NotImplemented('Method not implemented')
