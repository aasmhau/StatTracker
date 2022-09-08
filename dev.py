import os
import msvcrt
from data import DataStructures as ds


class Menu:

    def __init__(self):
        self.menuOptions = ['Register Match', 'Exit'] 

    def displayAndPickFromTable(self, optionList: list) -> int:
        os.system('cls')
        asciiInt = 97
        for option in optionList:
            print("{}  -  {}".format(chr(asciiInt), option))
            asciiInt += 1
        print("Esc  -  Cancel\nBackspace  -  Go back")

        selection = int(ord(msvcrt.getch())) - 97
        if selection == -89: # Backspace
            self.userMenu()
        if selection == -70: # Esc
            self.userMenu()
        while(selection < 0 or selection > len(optionList)-1):
            selection = int(ord(msvcrt.getch())) - 97
        return optionList[selection] 


    def userMenu(self):
        while(True):
            menuSelection = self.displayAndPickFromTable(self.menuOptions)

            match menuSelection:
                case 'Register Match':
                    self.registerMatch()
                case 'Exit':
                    print("Thank you for using this program!")
                    break


    def registerMatch(self): # Make it possible to go back with backspace, or cancel with escape
        selectedMode = self.displayAndPickFromTable(ds.maps)

if __name__ == "__main__":
    menu = Menu()
    menu.userMenu()


