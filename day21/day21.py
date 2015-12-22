import math

boss_hp, boss_damage, boss_armor = 103.0, 9, 2
# format for items is [cost, damage, armor]
# must use a weapon so not considering [0, 0, 0]
weapons = (8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74 ,8 ,0)
rings = (0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)
armors = (0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)

def config():
    for a in weapons:
        for b in armors:
            for c in rings:
                for d in rings:
                    # no same ring twice
                    if c == d and sum(c):
                        continue
                    # yield cost, damage, armor
                    yield a[0] + b[0] + c[0] + d[0], a[1] + b[1] + c[1] + d[1], a[2] + b[2] + c[2] + d[2], c[0]+d[0]

part1 = 1000
part2 = 0

# loop all possible equipments
for cost, damage, armor, ring in config():
    boss_dies = math.ceil(boss_hp / max(1, damage - boss_armor))
    player_dies = math.ceil(100.0 / max(1, boss_damage - armor))
    if player_dies >= boss_dies:
        part1 = min(part1, cost)
    else:
        part2 = max(part2, cost)
   
print part1, part2
