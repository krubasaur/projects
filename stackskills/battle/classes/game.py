import random


# ASSIGNS COLORS TO TERMINAL OUTPUT

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'           # ENDS THE COLOR SET FOR A STRING
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# PERSON: USED TO DEFINE BOTH ENIMIES AND OUR OWN PLAYER CHAR

class Person:

    # OFF THE BAT, WE KNOW WE NEED TO INIT THIS PERSON WITH STATS

    def __init__(self, hp, mp, atk, df, magic, items):

        # SETTING INSTANCE VARIABLES

        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ['Attack', 'Use Magic', 'Items']
        self.items = items

# CREATE UTILITY METHODS TO HANDLE DIFFERENT ACTIONS IN BATTLE

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

# GENERATES RANDOM DAMAGE BASED ON [PERSON]'S INSTANCE VARIABLES


# BELOW, TAKES FROM [MAGIC] ARRAY AND CALLS AN INDEX ITEM
#     def generate_spell_damage(self, i):
#         mgl = self.magic[i]['dmg'] - 5
#         mgh = self.magic[i]['dmg'] + 5
#         return random.randrange(mgl, mgh)

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def take_damage(self, dmg):
       # TAKES AWAY DAMAGE FROM THE HP
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp


# UTILITY CLASSES TO GET PROPERTIES
    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    # REDUCE MP WHEN USING [GENERATE_SPELL_DAMAGE]

    def reduce_mp(self, cost):
        self.mp -= cost

    # def get_spell_name(self, i):
    #     return self.magic[i]['name']
    #
    # def get_spell_mp_cost(self, i):
    #     return self.magic[i]['cost']

    def choose_action(self):
        i = 1
        print '\n' + bcolors.OKBLUE + bcolors.BOLD + "ACTIONS: " + bcolors.ENDC
        for item in self.actions:
            print '    ' + str(i) + '. ', item
            i += 1

    def choose_magic(self):
        i = 1

        print '\n' + bcolors.OKBLUE + bcolors.BOLD + "MAGIC: " + bcolors.ENDC
        for spell in self.magic:
            print '    ' + str(i) + '. ' + spell.name + ' (cost: ' + str(int(spell.cost)) + ')'
            i += 1

    def choose_item(self):
        i = 1
        print '\n' + bcolors.OKGREEN + bcolors.BOLD + 'ITEMS:' + bcolors.ENDC
        for item in self.items:
            print '    ' + str(i) + '. ' + item['item'].name + ' : ' + item['item'].descrip + ' ' + str(item['qt'])
            i += 1