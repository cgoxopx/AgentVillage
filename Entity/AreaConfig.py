from random import randint
from Entity.Chef.Chef import Chef
from Entity.Architect.Architect import Architect
from Entity.Building.MainTower import MainTower
from Entity.Farmer.Farmer import Farmer
from Entity.Flower import Flower
from Entity.Forest import Forest
from Entity.Sodier.Sodier import Soldier
from Entity.Stone import Stone
from Vector2 import Vector2


class AreaConfig:

    def __init__(self, world, WHOLE_MAP_SIZE, image_class):

        # Create Forest
        # for i in range(100):
        #     x = randint(100, WHOLE_MAP_SIZE[0] - 100)
        #     y = randint(100, WHOLE_MAP_SIZE[1] - 100)
        #     random_location = Vector2(x, y)
        #     forest = Forest(world, image_class.forest_img, random_location)
        #     world.add(forest)
        #     print("forest = Forest(world, image_class.forest_img, %r)\nworld.add(forest)" % forest.location)
        forest = Forest(world, image_class.forest_img, Vector2(1503, 3388))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(1000, 300))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(1564, 2139))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(8591, 2893))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(489, 4610))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(1067, 1181))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(1813, 1156))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(6526, 1358))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(7230, 1227))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(9075, 423))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(1436, 3832))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(8615, 5055))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(936, 1673))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(1851, 4110))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(840, 3602))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(9388, 3527))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(3507, 2405))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(6034, 611))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(1442, 3443))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(7126, 1274))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(3699, 1328))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(4737, 5296))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(3217, 4758))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(1671, 2398))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(2556, 5046))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(4223, 135))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(5317, 304))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(7379, 4047))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(216, 2560))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(6370, 2863))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(4186, 1184))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(8346, 3449))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(6856, 4616))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(5528, 4737))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(4427, 579))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(9441, 2348))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(4045, 4436))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(2192, 3110))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(9258, 1326))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(8427, 2952))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(6000, 1055))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(4869, 664))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(5055, 3599))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(3323, 1758))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(6339, 1531))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(5825, 5011))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(8868, 4169))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(5952, 157))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(2470, 1983))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(6128, 3726))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(3321, 4575))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(1477, 2588))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(1364, 3060))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(4130, 3785))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(8318, 1606))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(7219, 921))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(4794, 2663))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(8762, 3958))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(2385, 1908))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(636, 3011))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(5910, 2891))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(8491, 1961))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(9324, 3530))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(1011, 2472))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(131, 4490))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(398, 1924))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(2401, 959))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(848, 187))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(3017, 150))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(6806, 2800))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(5122, 1776))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(9270, 1856))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(377, 175))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(2434, 3903))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(5553, 438))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(6850, 840))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(5491, 4359))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(3290, 3427))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(4062, 3621))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(9280, 2668))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(3184, 5260))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(7092, 4506))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(2973, 3419))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(7703, 346))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(8846, 3182))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(9408, 4638))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(4698, 3338))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(2576, 4531))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(5658, 1071))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(253, 2295))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(5663, 1883))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(5044, 3243))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(4488, 1910))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(3106, 2475))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(8181, 4447))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(124, 1549))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(6982, 1977))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(1308, 611))
        world.add(forest)
        forest = Forest(world, image_class.forest_img, Vector2(2697, 3926))
        world.add(forest)

        # Create Stone
        # for i in range(50):
        #     x = randint(100, WHOLE_MAP_SIZE[0] - 100)
        #     y = randint(100, WHOLE_MAP_SIZE[1] - 100)
        #     random_location = Vector2(x, y)
        #     stone = Stone(world, image_class.stone_img, random_location)
        #     world.add(stone)
        #     print("stone = Stone(world, image_class.stone_img, %r)\nworld.add(stone)" % stone.location)
        stone = Stone(world, image_class.stone_img, Vector2(1200, 400))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(150, 425))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(3435, 1513))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(3783, 1710))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(9067, 5067))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(662, 1391))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(8423, 1245))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(303, 865))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(9108, 3650))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(5196, 1381))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(5015, 2931))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(5325, 1940))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(1704, 981))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(1713, 2066))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(6147, 2419))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(1741, 3724))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(3749, 2456))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(8154, 4951))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(4887, 3820))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(6263, 1675))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(4538, 2810))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(8220, 1667))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(466, 4514))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(5237, 3118))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(1532, 4783))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(3330, 1981))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(5262, 1593))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(8650, 3104))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(9255, 117))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(7340, 4752))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(3778, 507))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(3234, 4012))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(3798, 2234))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(1952, 4215))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(2091, 4451))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(6162, 1490))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(6902, 3241))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(4574, 4317))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(2340, 5133))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(7758, 4702))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(691, 3386))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(827, 1770))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(6971, 1312))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(5258, 3477))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(1205, 1557))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(3016, 1945))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(8397, 2268))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(5670, 4953))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(7559, 2018))
        world.add(stone)
        stone = Stone(world, image_class.stone_img, Vector2(1507, 742))
        world.add(stone)

        # Create Flower
        for i in range(20):
            x = randint(100, WHOLE_MAP_SIZE[0] - 100)
            y = randint(100, WHOLE_MAP_SIZE[1] - 100)
            random_location = Vector2(x, y)
            flower = Flower(world, image_class.flower_img, random_location)
            world.add(flower)
        flower = Flower(world, image_class.flower_img, Vector2(1207, 502))
        world.add(flower)

        # Create Berry
        for i in range(20):
            x = randint(100, WHOLE_MAP_SIZE[0] - 100)
            y = randint(100, WHOLE_MAP_SIZE[1] - 100)
            random_location = Vector2(x, y)
            berry = Flower(world, image_class.berry_img, random_location)
            world.add(berry)
        berry = Flower(world, image_class.berry_img, Vector2(1107, 600))
        world.add(berry)

        # Create Main Tower
        main_tower = MainTower(world, image_class.main_tower_img, Vector2(2200, 1200))
        world.add(main_tower)

        # house = House(world, image_class.house_img, Vector2(600, 650))
        # world.add(house)

        # Create Farmer
        for i in range(10):
            x = randint(-50, 50)
            y = randint(-50, 50)
            random_location = main_tower.location + Vector2(x, y)
            farmer = Farmer(world, image_class.farmer_lb_img, random_location)
            main_tower.add(farmer)
            farmer.brain.set_state("goCutting")
            world.add(farmer)

        # Create Soldier
        for i in range(5):
            x = randint(-50, 50)
            y = randint(-50, 50)
            random_location = main_tower.location + Vector2(x, y)
            soldier = Soldier(world, image_class.soldier_rb_img, random_location)
            main_tower.add(soldier)
            soldier.brain.set_state("patrol")
            world.add(soldier)

        # Create Architect
        for i in range(5):
            x = randint(-50, 50)
            y = randint(-50, 50)
            random_location = main_tower.location + Vector2(x, y)
            architect = Architect(world, image_class.architect_rb_img, random_location)
            main_tower.add(architect)
            architect.brain.set_state("free")
            world.add(architect)

        # Create Chef
        x = randint(-50, 50)
        y = randint(-50, 50)
        random_location = main_tower.location + Vector2(x, y)
        chef = Chef(world, image_class.chef_lb_img, random_location)
        main_tower.add(chef)
        chef.brain.set_state("free")
        world.add(chef)
