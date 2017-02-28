from .model_enums import ModelEnum, EnumValue

class ProjectStates(ModelEnum):
    NEW         = EnumValue('new', 'New')
    ACTIVE      = EnumValue('act', 'Active')
    PAUSED      = EnumValue('pau', 'Paused')
    ARCHIVED    = EnumValue('arc', 'Archived')
