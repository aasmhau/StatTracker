import os
import platform


"""
Ideas:

Add current date and time when writing to file
"""

class Maps:
    def __init__(self):
        """
        A class keeping every possible gamemode and map, and lets the player select 
        the played map for statistical analysis
        """
        self.escort = ['Circuit Royal', 
                       'Dorado', 
                       'Havana', 
                       'Junkertown', 
                       'Rialto', 
                       'Route 66',
                       'Gothenburg']

        self.hybrid = ['Blizzard World', 
                       'Eichenwalde', 
                       'Hollywood', 
                       'King\'s Row', 
                       'Midtown', 
                       'Numbani', 
                       'Paraiso']

        self.control = ['Busan', 
                        'Ilios', 
                        'Lijiang Tower', 
                        'Nepal', 
                        'Oasis']

        self.push = ['Colosseo', 
                     'New Queen Street', 
                     'Portugal']



        self.mode = [self.escort, self.hybrid, self.control, self.push]
        self.modes = ['Escort', 'Hybrid', 'Control', 'Push']
        
    def chooseGamemode(self):
        self.clear()
        modeNumber = 97
        for mode_ in self.modes:
            print("{}  -  {}".format(chr(modeNumber), mode_))
            modeNumber += 1
        gamemode = int(ord(input(("> ")))) - 97 

        self.clear()
        mapNumber = 97
        for map_ in self.mode[gamemode]:
            print("{}  -  {}".format(chr(mapNumber), map_))
            mapNumber += 1
        mapSelect = int(ord(input(("> ")))) - 97

    def clear(self):
        if platform.system() == 'Linux':
            os.system('clear')
        elif platform.system() == 'Windows':
            os.system('cls')
        

if __name__ == "__main__":
    maps = Maps()
    maps.chooseGamemode()

