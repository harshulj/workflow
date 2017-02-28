from projects. model_enums import ModelEnum, EnumValue

class FlowTypes(ModelEnum):
    CATEGORIZATION  = EnumValue('cat', 'Categorization')
    ATTRIBUTES      = EnumValue('att', 'Attributes')

class RuleOperations(ModelEnum):
    IN                  = EnumValue('in', 'In')
    EQUALS              = EnumValue('eq', 'Equals')
    EQUALS_INT          = EnumValue('eqi', 'Equals Integer')
    LESS_THAN           = EnumValue('th', 'Less Than')
    LESS_THAN_EQUALS    = EnumValue('the', 'Less Than Equals')
    GRATER_THAN         = EnumValue('gt', 'Greater Than')
    GRATER_THAN_EQUALS  = EnumValue('gte', 'Greater Than Equals')
    MATCHES_REGEX       = EnumValue('mrx', 'Matches regex')
