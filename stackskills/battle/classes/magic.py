import random

class Spell:
    # CAN BE USED AS SYSTEMS. SYSTEM(NAME, ACCESS, PROVISIONER) BUT WHAT ABOUT SPECIAL CASE INSTRUCTIONS?
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_damage(self, i):

        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)