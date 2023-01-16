from models import BaseModel


class Round16(BaseModel):

    def __init__(self, groups=None):
        super().__init__(groups)
        self.team_number = 16
        self.stage_name = "Round 16"
