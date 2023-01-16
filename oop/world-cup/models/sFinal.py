from models import ModelWithIdenticalBuildMethod

class sFinal(ModelWithIdenticalBuildMethod):

    def __init__(self, groups=None):
        super().__init__(groups)
        self.team_number = 4
        self.stage_name = 'sFinal'

  
