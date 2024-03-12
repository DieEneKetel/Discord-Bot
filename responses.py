from random import randint
from rand_char import player, rand_class , rand_name ,rand_stats

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if 'roll' in lowered:
        roll = randint(1,20)
        print(f'rolled: {roll}')
        if roll == 20:
            return f'You rolled a [{roll}] CRITICAL HIT!'
        elif roll == 1:
            return f'You rolled a [{roll}] CRITICAL FALIURE!'
        else:
            return f'You rolled a [{roll}]'
        
    if 'random character' in lowered:
        
        MaxName = len(rand_name)-1
        MaxClass = len(rand_class)-1
        MaxStats = len(rand_stats)-1

        Name = randint(0,MaxName)
        Class = randint(0,MaxClass)
        Stats = randint(0,MaxStats)

        Health = rand_stats[Stats][0]
        Agility = rand_stats[Stats][1]
        Strength = rand_stats[Stats][2]
        Magic = rand_stats[Stats][3]
        Special = rand_stats[Stats][4]

        Player = player(f'{rand_name[Name]}', f'{rand_class[Class]}', Health, Agility, Strength, Magic, Special)

        playerData = f"Name: {Player.Name} \nClass: {Player.Class} \nHealth: {Player.Health} \nAgility: {Player.Agility} \nStrength: {Player.Strength} \nMagic: {Player.Magic} \nSpecial: {Player.Special}"

        print(playerData)
        return f"{playerData}"
