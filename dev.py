import os
import time
import msvcrt
from tkinter import W
from data import DataStructures as ds

class Menu:

    def __init__(self):
        self.menuOptions = ['Register Match', 'Exit'] 

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
        if selection == -70: # Esc
            self.userMenu()
        while(selection < 0 or selection > len(optionList)-1):
            selection = int(ord(msvcrt.getch())) - 97
        return currentOptions[selection] 


    def userMenu(self):
        while(True):
            menuSelection = self.displayAndPickFromTable(self.menuOptions)

            match menuSelection:
                case 'Register Match':
                    self.registerMatch()
                case 'Exit':
                    print("Thank you for using this program!")
                    exit(1)


    def registerMatch(self): # Make it possible to go back with backspace, or cancel with escape
        selectedMode = self.displayAndPickFromTable(ds.maps)
        selectedMap = self.displayAndPickFromTable(ds.maps[selectedMode])
        selectedRole = self.displayAndPickFromTable(ds.heroes)
        selectedHero = self.displayAndPickFromTable(ds.heroes[selectedRole])

        print("{}-{}-{}-{}".format(selectedMode, selectedMap, selectedRole, selectedHero))
        time.sleep(2)


if __name__ == "__main__":
    menu = Menu()
    menu.userMenu()


