class ControlState():

    CURRENT_TEAM = ""

    BOMB_PLANTED = "bomb_planted"

    ROUND_OVER_WINNER = "round_over_winner"
    ROUND_OVER_LOSER = "round_over_loser"

    FREEZE = "freeze"
    LIVE = "live"

    FLASHED = "flashed"
    BURNING = "burning"
    SMOKED = "smoked"

    # STATE_STACK = {
    #     BOMB_PLANTED: 1,
    #     ROUND_OVER_WINNER: 1,
    #     ROUND_OVER_LOSER: 1,
    #     FREEZE: 1,
    #     LIVE: 1,
    #     FLASHED: 1,
    #     BURNING: 1,
    #     SMOKED: 1
    # }

    def __init__(self):
        self.current_states = []

class State():

    def __init__(self, name = None, ):
        self.name = ""
