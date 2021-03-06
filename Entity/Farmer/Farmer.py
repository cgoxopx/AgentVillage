from Entity.Farmer.FarmerState import FarmerStateGoCutting, FarmerStateCutting, FarmerStateReturning
from GameEntity import GameEntity
from StateMachine import StateMachine


class Farmer(GameEntity):

    def __init__(self, world, farmer_image, location):
        GameEntity.__init__(self, "farmer", world, farmer_image)
        self.location = location
        self.color = (0, 0, 200)
        self.brain = StateMachine()
        self.forest_id = None
        self.stone_id = None
        self.max_bear_load = 10
        self.bear_load = self.max_bear_load
        stateGoCutting = FarmerStateGoCutting(self)
        stateCutting = FarmerStateCutting(self)
        stateReturning = FarmerStateReturning(self)
        self.brain.add_state(stateGoCutting)
        self.brain.add_state(stateCutting)
        self.brain.add_state(stateReturning)
        self.time_passed = 0
        self.main_tower = None
        self.hp = 10

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)

    def process(self, time_passed):
        GameEntity.process(self, time_passed)
        self.time_passed = time_passed

    def bitten(self):
        self.hp -= 1
        if self.hp <= 0:
            self.world.remove(self.id)
            self.main_tower.people_list.remove(self)
            del self
