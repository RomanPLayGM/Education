number_of_units, unlucky_number_of_units = map(int, input().split())
max_damage = 0
so_close_set = set(range(1, number_of_units)) - {unlucky_number_of_units}
clear_set = filter(lambda units: number_of_units % units != unlucky_number_of_units, so_close_set)
for units in clear_set:
    damage = units ** (number_of_units // units)
    if number_of_units % units != 0:
        damage = damage * (number_of_units % units)
    # print(damage)
    if max_damage < damage:
        max_damage = damage
print(max_damage)
