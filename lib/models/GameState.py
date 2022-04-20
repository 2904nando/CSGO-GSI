class GameState():

    def update(self, **game_state_response):
        self.provider = Provider(**game_state_response.get('provider', {}))
        self.map = Map(**game_state_response.get('map', {}))
        self.map_round_wins = MapRoundWins(**game_state_response.get('map_round_wins', {}))
        self.round = Round(**game_state_response.get('round', {}))
        self.player = Player(**game_state_response.get('player', {}))
        self.previous = Previous(**game_state_response.get('previously', {}))
        self.added = Added(**game_state_response.get('added', {}))

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
        self.weapons = PlayerWeapons(**kwargs.get('weapons', {}))
        self.stats = PlayerStats(**kwargs.get("match_stats", {}))

class PlayerStats():

    def __init__(self, **kwargs):
        self.kills = kwargs.get("kills", 0)
        self.assists = kwargs.get("assists", 0)
        self.deaths = kwargs.get("deaths", 0)
        self.mvps = kwargs.get("mvps", 0)
        self.score = kwargs.get("score", 0)

class PlayerState():
    
    def __init__(self, **kwargs):
        self.health = kwargs.get('health', None)
        self.armor = kwargs.get('armor', None)
        self.flashed = kwargs.get('flashed', None)
        self.smoked = kwargs.get('smoked', None)
        self.burning = kwargs.get('burning', None)
        self.money = kwargs.get('money', None)

class PlayerWeapons():

    def __init__(self, **kwargs):
        weapons = sorted([Weapon(**kwargs[key]) for key in kwargs.keys() if kwargs[key]], key=lambda x: x.state)

        self.on_hand = weapons[0] if len(weapons)>0 else {}
        weapons.pop(0)

        self.grenades = [weapon for weapon in weapons if weapon.type == "Grenade"]
        weapons = list(filter(lambda weapon: weapon.type != "Grenade", weapons))

        self.pistols = [weapon for weapon in weapons if weapon.type == "Pistol"]
        weapons = list(filter(lambda weapon: weapon.type != "Pistol", weapons))

        self.primary = [weapon for weapon in weapons if weapon.type in ["Rifle", "Shotgun", "Submachine Gun"]]
        weapons = list(filter(lambda weapon: weapon.type not in ["Rifle", "Shotgun", "Submachine Gun"], weapons))

        self.other = weapons

class Weapon():

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', "")
        self.type = kwargs.get('type', "")
        self.ammo_clip = kwargs.get('ammo_clip', None)
        self.ammo_clip_max = kwargs.get('ammo_clip_max', None)
        self.ammo_reserve = kwargs.get('ammo_reserve', None)
        self.state = kwargs.get('state', "")
        
class Previous():

    def __init__(self, **kwargs):
        self.udpated_topics = list(kwargs.keys())

class Added():

    def __init__(self, **kwargs):
        self.added_topics = list(kwargs.keys())