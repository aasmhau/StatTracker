import os
import time
import msvcrt
from tkinter import W
from data import DataStructures as ds


class Menu:

    def __init__(self):
        self.menuOptions = ['Register Match', 'Exit']

    escort = ['Circuit Royal',
              'Dorado',
              'Havana',
              'Junkertown',
              'Rialto',
              'Route 66',
              'Gothenburg']

    hybrid = ['Blizzard World',
              'Eichenwalde',
              'Hollywood',
              'King\'s Row',
              'Midtown',
              'Numbani',
              'Paraiso']

    control = ['Busan',
               'Ilios',
               'Lijiang Tower',
               'Nepal',
               'Oasis']

    push = ['Colosseo',
            'New Queen Street',
            'Portugal']

    tank = ['D.Va',
            'Doomfist',
            'Junker Queen',
            'Orisa',
            'Reinhardt',
            'Roadhog',
            'Sigma',
            'Winston',
            'Wrecking Ball',
            'Zarya']

    dps = ['Ashe',
           'Bastion',
           'Cassidy',
           'Echo',
           'Genji',
           'Hanzo',
           'Junkrat',
           'Mei',
           'Phara',
           'Reaper',
           'Soldier: 76',
           'Sojourn',
           'Sombra',
           'Symmetra',
           'Torbjorn',
           'Tracer',
           'Widowmaker']

    support = ['Ana',
               'Baptiste',
               'Brigitte',
               'Lucio',
               'Mercy',
               'Moira',
               'Zenyatta']

    maps = {'Escort': escort, 'Hybrid': hybrid,
            'Control': control, 'Push': push}
    heroes = {'Tank': tank, 'DPS': dps, 'Support': support}
    results = ['Victory', 'Defeat', 'Draw']

    def displayAndPickFromTable(self, optionList: list) -> int:
        os.system('cls')
        asciiInt = 97
        currentOptions = []
        print("Esc  -  Cancel")
        for option in optionList:
            currentOptions.append(option)
            print("{}  -  {}".format(chr(asciiInt), option))
            asciiInt += 1

        selection = int(ord(msvcrt.getch())) - 97
        if selection == -70:  # Esc
            self.userMenu()
        while (selection < 0 or selection > len(optionList)-1):
            selection = int(ord(msvcrt.getch())) - 97
        return currentOptions[selection]

    def userMenu(self):
        while (True):
            menuSelection = self.displayAndPickFromTable(self.menuOptions)

            match menuSelection:
                case 'Register Match':
                    self.registerMatch()
                case 'Exit':
                    print("Thank you for using this program!")
                    exit(0)

    # Make it possible to go back with backspace, or cancel with escape
    def registerMatch(self):
        selectedMode = self.displayAndPickFromTable(ds.maps)
        selectedMap = self.displayAndPickFromTable(ds.maps[selectedMode])
        selectedRole = self.displayAndPickFromTable(ds.heroes)
        selectedHero = self.displayAndPickFromTable(ds.heroes[selectedRole])

        print("{}-{}-{}-{}".format(selectedMode,
              selectedMap, selectedRole, selectedHero))
        time.sleep(2)


if __name__ == "__main__":
    menu = Menu()
    menu.userMenu()
