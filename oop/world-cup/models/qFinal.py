from models import ModelWithIdenticalBuildMethod

class qFinal(ModelWithIdenticalBuildMethod):

    def __init__(self, groups=None):
        super().__init__(groups)
        self.stage_name = "qFinal"
        self.team_number = 8

    
