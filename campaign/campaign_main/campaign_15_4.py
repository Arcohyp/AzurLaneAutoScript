from module.campaign.campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger
# from .campaign_15_1 import Config as ConfigBase

MAP = CampaignMap('15-4')
MAP.shape = 'K9'
MAP.camera_data = ['E4', 'C8', 'H2', 'H6', 'H7']
MAP.camera_data_spawn_point = ['H2']
MAP.map_data = """
    ME -- ME ME Me -- ME ++ ++ ME ME
    ME -- -- -- -- ME -- ++ ++ -- ME
    ++ -- -- -- -- -- ME SP SP ME Me
    ++ ME -- ++ ++ -- -- -- -- ME --
    -- Me ME MA ++ ME -- -- -- -- ME
    ME ME ME -- -- -- -- ++ ME -- Me
    ME -- __ -- ME ME -- ME ME -- ++
    -- -- ++ -- Me -- ME ME ME ME --
    MB Me -- ME ME Me ++ ++ ++ -- ME
"""
MAP.weight_data = """
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 5, 'mystery': 2},
    {'battle': 1, 'enemy': 1},
    {'battle': 2, 'enemy': 1},
    {'battle': 3, 'enemy': 1},
    {'battle': 4},
    {'battle': 5},
    {'battle': 6},
    {'battle': 7, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, I1, J1, K1, \
A2, B2, C2, D2, E2, F2, G2, H2, I2, J2, K2, \
A3, B3, C3, D3, E3, F3, G3, H3, I3, J3, K3, \
A4, B4, C4, D4, E4, F4, G4, H4, I4, J4, K4, \
A5, B5, C5, D5, E5, F5, G5, H5, I5, J5, K5, \
A6, B6, C6, D6, E6, F6, G6, H6, I6, J6, K6, \
A7, B7, C7, D7, E7, F7, G7, H7, I7, J7, K7, \
A8, B8, C8, D8, E8, F8, G8, H8, I8, J8, K8, \
A9, B9, C9, D9, E9, F9, G9, H9, I9, J9, K9, \
    = MAP.flatten()


class Config:
    HOMO_EDGE_COLOR_RANGE = (0, 49)
    HOMO_EDGE_HOUGHLINES_THRESHOLD = 210

    # Disabled because having errors
    MAP_SWIPE_PREDICT_WITH_SEA_GRIDS = False
    # Ambushes can be avoid by having more DDs.
    MAP_WALK_OPTIMIZE = False
    # ===== Start of generated config =====
    MAP_HAS_SIREN = False
    MAP_HAS_MOVABLE_ENEMY = False
    MAP_HAS_MAP_STORY = False
    MAP_HAS_FLEET_STEP = False
    MAP_HAS_AMBUSH = True
    MAP_HAS_MYSTERY = True
    # ===== End of generated config =====


class Campaign(CampaignBase):
    MAP = MAP
    ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'

    """
    Using F1 to battle with 1st and 3rd boss
    Using F2 to battle with 2nd boss
    The whole battle process is:
        F1: 0 1 2 3(1st boss) 4 5 7 8(3rd boss) 
        F2: 6(2nd boss)
    """

    def battle_0(self):
        self.expel_target(J8, I8)
        self.clear_chosen_enemy(K9)
        return self.battle_default()

    def battle_1(self):
        self.clear_chosen_enemy(A1)
        return self.battle_default()

    def battle_3(self):
        self.clear_chosen_enemy(H5)
        self.pick_up_ammo()

        return self.battle_default()

    # F1: 4 5
    # 4,5 = normal

    # F2: 6
    def battle_6(self):
        # switch to fleet 2
        self.fleet_boss.clear_chosen_enemy(D3)
        # switch to fleet 1
        return self.battle_default()

    # F1: 7 8
    # 7 = normal
    def battle_8(self):
        return self.clear_boss()
