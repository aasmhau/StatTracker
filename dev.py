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
        self.heroes = {'Tank': self.tank,
                       'DPS': self.dps, 'Support': self.support}
        self.results = ['Victory', 'Defeat', 'Draw']

    def displayAndPickFromTable(self, option_list: list) -> int:
        os.system('cls')
        ascii_int = 97
        current_options = []
        print("Esc  -  Cancel")
        for option in option_list:
            current_options.append(option)
            print("{}  -  {}".format(chr(ascii_int), option))
            asciiInt += 1

        selection = int(ord(msvcrt.getch())) - 97
        if selection == -70:  # Esc
            self.userMenu()
        while (selection < 0 or selection > len(option_list)-1):
            selection = int(ord(msvcrt.getch())) - 97
        return current_options[selection]

    def userMenu(self):
        while True:
            menuSelection = self.displayAndPickFromTable(self.menuOptions)
            match menuSelection:
                case 'Register Match':
                    self.registerMatch()
                case 'Exit':
                    print("Thank you for using this program!")
                    exit(0)

    # Make it possible to go back with backspace, or cancel with escape
    def registerMatch(self):
        selected_mode = self.displayAndPickFromTable(self.maps)
        selected_map = self.displayAndPickFromTable(self.maps[selected_mode])
        selected_role = self.displayAndPickFromTable(self.heroes)
        selected_hero = self.displayAndPickFromTable(
            self.heroes[selected_role])

        print("{}-{}-{}-{}".format(selected_mode,
              selected_map, selected_role, selected_hero))
        time.sleep(2)


if __name__ == "__main__":
    menu = Menu()
    menu.userMenu()
