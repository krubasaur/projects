from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

fire = Spell('fire', 10, 100, 'black')
thunder = Spell('thunder', 10, 124, 'black')
blizzard = Spell('blizzard', 10, 100, 'black')
meteor = Spell('meteor', 10, 150, 'black')
quake = Spell('quake', 10, 160, 'black')

cure = Spell('cure', 12, 120, 'white')
cura = Spell('cura', 18, 200, 'white')

potion = Item('Potion', 'potion', 'heals 50 HP', 50)
hipotion = Item('Hi-Potion', 'potion', 'heals 100 HP', 100)
superpotion = Item('Super Potion', 'potion', 'heals 500 HP', 500)
elixir = Item('Elixir', 'elixir', 'fully restores HP/MP of one party member', 9999)
megaelixir = Item('Mega Elixir', 'elixir', 'fully restores party\'s HP/MP', 9999)

grenade = Item('Grenade', 'attack', 'deals 500 damage', 500)

# INSTANTIATE THE PERSON CLASS WITH HP, MAGIC POINTS, ATTACK POWER,
# DEFENSE POWER AND MAGIC SPELL

player_magic = [fire, thunder, blizzard, cure, cura]
player_items = [{'item': grenade, 'qt': 5}, {'item': potion, 'qt': 5},
                {'item': hipotion, 'qt': 5}, {'item': superpotion, 'qt': 5},
                {'item': elixir, 'qt': 5}, {'item': megaelixir, 'qt': 5}]

player = Person(460, 65, 60, 34, player_magic, player_items)

enemy = Person(1200, 65, 45, 25, [], [])

i = 0

running = True

print bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS!' + bcolors.ENDC

while running:
    print "========================================="
    player.choose_action()

    choice = int(raw_input('Choose Action: ')) - 1


    if choice == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)  # TAKES RANDOM NUMBER BETWEEN ATKH & ATKL TO GENERATE DAMAGE FOR SPECIFIC INSTANCE (ENEMY IN THIS CASE)
        print 'You attacked for ', dmg, ' points of HP. Enemy HP: ', enemy.get_hp()

    elif choice == 1:
        player.choose_magic()
        magic_choice = int(raw_input('Choose magic:')) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage(magic_choice)


        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print bcolors.FAIL, '\nNot enough MP\n', bcolors.ENDC
            continue


        player.reduce_mp(spell.cost)

        if spell.type == 'white':
            player.heal(magic_dmg)
            print bcolors.OKBLUE, '\n', spell.name, 'heals for ', str(magic_dmg), 'HP.', bcolors.ENDC
        elif spell.type == 'black':
            enemy.take_damage(magic_dmg)
            print bcolors.OKBLUE, '\n', spell.name, 'deals ', str(magic_dmg), 'points of damage.', bcolors.ENDC

        # enemy.take_damage(magic_dmg)
        #
        # # print bcolors.OKBLUE, '\n', spell.name, ' deals ', str(magic_dmg), ' points of damage.', bcolors.ENDC
        # #
        # # enemy_hp = enemy.get_hp()
        # #
    elif choice == 2:
        player.choose_item()
        item_choice = int(raw_input('Choose item: ')) - 1

        if item_choice == -1:
            continue

        if player.items[item_choice]['qt'] == 0:
            print bcolors.FAIL + '\n' + 'None left...' + bcolors.ENDC
            continue

        item = player.items[item_choice]['item']
        player.items[item_choice]['qt'] -= 1


        if item.type == 'potion':
            player.heal(item.prop)
            print bcolors.OKGREEN + '\n' + item.name + ' heals for ', str(item.prop) + ' HP' + bcolors.ENDC

        elif item.type == 'elixir':
            player.hp = player.maxhp
            player.mp = player.maxmp
            print bcolors.OKGREEN + '\n' + item.name + ' fully restores HP/MP' + bcolors.ENDC

        elif item.type == 'attack':
            enemy.take_damage(item.prop)
            print bcolors.FAIL + '\n' + item.name + ' deals enemy' + str(item.prop) + ' points damage' + bcolors.ENDC

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print 'Enemy attacks for ', enemy_dmg, 'Player HP ', player.get_hp()

    print '---------------------------'
    print 'Enemy HP: ', bcolors.FAIL, str(enemy.get_hp()), '/', str(enemy.maxhp), bcolors.ENDC
    print '---------------------------'
    print 'Your HP: ', bcolors.OKGREEN, str(player.get_hp()), '/', str(player.maxhp), bcolors.ENDC
    print 'Your MP: ', bcolors.OKBLUE, str(player.get_mp()), '/', str(player.maxmp), bcolors.ENDC

    if enemy.get_hp() == 0:
        print bcolors.OKGREEN + 'You win!' + bcolors.ENDC
        running = False

    elif player.get_hp() == 0:
        print bcolors.FAIL + 'You DIED!' + bcolors.ENDC
        running = False


    # running = False
#
# print 'player damage ' + str(player.generate_damage())
# print str(player.generate_damage())
# print str(player.generate_damage())
#
# print str(player.generate_spell_damage(0))
# print str(player.generate_spell_damage(2))