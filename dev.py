import os
import time
import msvcrt

class Menu:

    def __init__(self):
        self.menuOptions = ['Register Match', 'Exit']
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

        self.tank = ['D.Va',
            'Doomfist',
            'Junker Queen',
            'Orisa',
            'Reinhardt',
            'Roadhog',
            'Sigma',
            'Winston',
            'Wrecking Ball',
            'Zarya']

        self.dps = ['Ashe',
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

        self.support = ['Ana',
               'Baptiste',
               'Brigitte',
               'Lucio',
               'Mercy',
               'Moira',
               'Zenyatta']

        self.maps = {'Escort': self.escort, 'Hybrid': self.hybrid,
            'Control': self.control, 'Push': self.push}
        self.heroes = {'Tank': self.tank, 'DPS': self.dps, 'Support': self.support}
        self.results = ['Victory', 'Defeat', 'Draw']

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
        selectedMode = self.displayAndPickFromTable(self.maps)
        selectedMap = self.displayAndPickFromTable(self.maps[selectedMode])
        selectedRole = self.displayAndPickFromTable(self.heroes)
        selectedHero = self.displayAndPickFromTable(self.heroes[selectedRole])

        print("{}-{}-{}-{}".format(selectedMode,
              selectedMap, selectedRole, selectedHero))
        time.sleep(2)


if __name__ == "__main__":
    menu = Menu()
    menu.userMenu()
