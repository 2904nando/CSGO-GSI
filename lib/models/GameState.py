class GameState():

    def update(self, **game_state_response):
        self.provider = Provider(**game_state_response.get('provider', {}))
        self.map = Map(**game_state_response.get('map', {}))
        self.map_round_wins = MapRoundWins(**game_state_response.get('map_round_wins', {}))
        self.round = Round(**game_state_response.get('round', {}))
        self.player = Player(**game_state_response.get('player', {}))
        self.previous = Previous(**game_state_response.get('previously', {}))

    def select_action(self):
        if self.previous.udpated_topics:
            pass
        else:
            return


class Provider():
    
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.timestamp = kwargs.get('timestamp', None)

class Map():
    
    def __init__(self, **kwargs):
        self.mode = kwargs.get('mode', '')
        self.name = kwargs.get('name', '')
        self.phase = kwargs.get('phase', '')
        self.round = kwargs.get('round', None)
        self.team_ct = MapTeam(**kwargs.get('team_ct', {}))
        self.team_t = MapTeam(**kwargs.get('team_t', {}))

class MapTeam():

    def __init__(self, **kwargs):
        self.score = kwargs.get('score', None)

class MapRoundWins():
    
    def __init__(self):
        pass

class Round():
    
    def __init__(self, **kwargs):
        self.phase = kwargs.get('phase', '')
        self.win_team = kwargs.get('win_team', '')
        self.bomb = kwargs.get('bomb', '')

class Player():
    
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.team = kwargs.get('team', '')
        self.activity = kwargs.get('activity', '')
        self.state = PlayerState(**kwargs.get('state', {}))

class PlayerState():
    
    def __init__(self, **kwargs):
        self.health = kwargs.get('health', None)
        self.armor = kwargs.get('armor', None)
        self.flashed = kwargs.get('flashed', None)
        self.smoked = kwargs.get('smoked', None)
        self.burning = kwargs.get('burning', None)
        self.money = kwargs.get('money', None)
        
class Previous():

    def __init__(self, **kwargs):
        self.udpated_topics = list(kwargs.keys())