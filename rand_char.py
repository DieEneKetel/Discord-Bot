from random import randint

class player:
    def __init__(self, Name, Class, Health, Agility, Strength, Magic, Special):
        self.Name = Name
        self.Class = Class
        self.Health = Health
        self.Agility = Agility
        self.Strength = Strength
        self.Magic = Magic
        self.Special = Special


rand_name = ['jeff', 'gorlack the destroyer', 'The maidenless', 'Ingrïd Destroyer of worlds']

rand_class = ['mage', 'warrior' , 'swordman']

rand_stats =    [
                    [5, 5, 5, 5, 5],

                    [6, 5, 5, 5, 4],
                    [5, 6, 5, 5, 4],
                    [5, 5, 6, 5, 4],
                    [5, 5, 5, 6, 4],

                    [6, 5, 5, 4, 5],
                    [5, 6, 5, 4, 5],
                    [5, 5, 6, 4, 5],
                    [5, 5, 5, 4, 6],

                    [6, 5, 4, 5, 5],
                    [5, 6, 4, 5, 5],
                    [5, 5, 4, 6, 5],
                    [5, 5, 4, 5, 6],

                    [6, 4, 5, 5, 5],
                    [5, 4, 6, 5, 5],
                    [5, 4, 5, 6, 5],
                    [5, 4, 5, 5, 6],

                    [4, 6, 5, 5, 5],
                    [4, 5, 6, 5, 5],
                    [4, 5, 5, 6, 5],
                    [4, 5, 5, 5, 6],
                    
                    [5, 4, 3, 7, 6],
                    [6, 5, 7, 3, 4],
                    [7, 6, 5, 4, 3]
                ]