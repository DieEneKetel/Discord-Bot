from random import randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if 'roll' in lowered:
        roll = randint(1,20)
        if roll == 20:
            return f'You rolled a [{roll}] CRITICAL HIT!'
        elif roll == 1:
            return f'You rolled a [{roll}] CRITICAL FALIURE!'
        else:
            return f'You rolled a [{roll}]'