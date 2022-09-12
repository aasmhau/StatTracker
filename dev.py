import os
import time
import sys
import msvcrt


class Menu:

    def __init__(self):
        self.menu_options = ['Register Match', 'Exit']
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

    def display_and_pick_from_table(self, option_list: list) -> int:
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
            self.user_menu()
        while (selection < 0 or selection > len(option_list)-1):
            selection = int(ord(msvcrt.getch())) - 97
        return current_options[selection]

    def user_menu(self):
        while True:
            menu_selection = self.display_and_pick_from_table(
                self.menu_options)

            if menu_selection == 'Register Match':
                self.register_match()
            elif menu_selection == 'Exit':
                print("Thank you for using this program!")
                sys.exit(0)

    # Make it possible to go back with backspace, or cancel with escape
    def register_match(self):
        selected_mode = self.display_and_pick_from_table(self.maps)
        selected_map = self.display_and_pick_from_table(
            self.maps[selected_mode])
        selected_role = self.display_and_pick_from_table(self.heroes)
        selected_hero = self.display_and_pick_from_table(
            self.heroes[selected_role])

        print(f"{selected_mode}-{selected_map}-{selected_role}-{selected_hero}")
        time.sleep(2)


if __name__ == "__main__":
    menu = Menu()
    menu.user_menu()
