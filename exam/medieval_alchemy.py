from collections import deque

substances = [int(x) for x in input().split(', ')]
crystals = deque([int(x) for x in input().split(', ')])
crafted_potions = []
all_crafted = False

potions = {
    "Brew of Immortality": 110,
    "Essence of Resilience": 100,
    "Draught of Wisdom": 90,
    "Potion of Agility": 80,
    "Elixir of Strength": 70
}

while substances and crystals:
    current_substance = substances[-1]
    current_crystal = crystals[0]
    total_energy = current_crystal + current_substance
    found_potion = False

    for potion, energy_needed in potions.items():
        if potion not in crafted_potions and total_energy >= energy_needed:
            if total_energy == energy_needed:
                crafted_potions.append(potion)
                crystals.popleft()
                substances.pop()
            else:
                crafted_potions.append(potion)
                substances.pop()
                new_energy = crystals.popleft() - 20
                if new_energy > 0:
                    crystals.append(new_energy)


            found_potion = True
            break

    if not found_potion:
        substances.pop()
        new_energy = crystals.popleft() - 5
        if new_energy > 0:
            crystals.append(new_energy)


    if len(crafted_potions) == 5:
        all_crafted = True
        break

if all_crafted:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions)}")

if substances:
    print(f"Substances: {(', '.join(map(str, substances[::-1])))}")
if crystals:
    print(f"Crystals: {(', '.join(map(str, crystals)))}")