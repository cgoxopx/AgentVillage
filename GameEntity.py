from Vector2 import Vector2
from StateMachine import StateMachine


class GameEntity:
    def __init__(self, name, world, image):
        self.world = world
        self.name = name
        self.image = image
        self.speed = 0
        self.location = Vector2(0, 0)
        self.destination = Vector2(0, 0)
        self.brain = StateMachine()
        self.id = 0
        self.main_tower = None

    def render(self, surface, start_draw_pos):
        if self.image:
            x = self.location.x
            y = self.location.y
            w, h = self.image.get_size()
            surface.blit(self.image, (x - w / 2 + start_draw_pos[0], y - h / 2 + start_draw_pos[1]))

    def process(self, time_passed):
        time_passed_second = time_passed / 1000
        self.brain.think()
        if self.destination != self.location:
            vec_to_destination = self.destination - self.location
            distance_to_destination = abs(vec_to_destination)
            heading = vec_to_destination.normalization()
            shifting_distance = min(distance_to_destination, self.speed * time_passed_second)
            self.location += heading * shifting_distance

    def is_over(self, other_location):
        x = self.location.x
        y = self.location.y
        w, h = self.image.get_size()
        if (x - w / 2) < other_location.x < (x + w / 2) and (y - h / 2) < other_location.y < (y + h / 2):
            return True
        return False
