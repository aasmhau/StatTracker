import os
import platform
import msvcrt


"""
Ideas:

if not studentName.isalpha():
    print("Only letters are allowed!")


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

    
    def select(self, alt):
        self.clear()
        modeNumber = 97
        for m in alt:
            print("{}  -  {}".format(chr(modeNumber), m))
            modeNumber += 1
        return int(ord(msvcrt.getch())) - 97

    def chooseGamemode(self):
        gamemode = self.select(self.modes)
        mapchoice = self.select(self.mode[gamemode])
        print(self.mode[gamemode][mapchoice]) 

    def clear(self):
        if platform.system() == 'Linux':
            os.system('clear')
        elif platform.system() == 'Windows':
            os.system('cls')
        

if __name__ == "__main__":
    maps = Maps()
    maps.chooseGamemode()

