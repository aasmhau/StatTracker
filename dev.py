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
        if selection == -89: # Backspace
            return -1
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
        print(self.selectMode())
        time.sleep(3)

    def selectMode(self):
        selectedMode = self.displayAndPickFromTable(ds.maps)
        if selectedMode == -1:
            self.registerMatch()
        return selectedMode + self.selectMap(selectedMode)

    def selectMap(self, mode): 
        selectedMap = self.displayAndPickFromTable(ds.maps[mode]) 
        if selectedMap == -1:
            self.selectMode()
        return selectedMap + self.selectRole(mode)

    def selectRole(self, mode):
        selectedRole = self.displayAndPickFromTable(ds.heroes)
        if selectedRole == -1:
            self.selectMap(mode)
        return selectedRole + self.selectHero(selectedRole)

    def selectHero(self, role):
        selectedHero = self.displayAndPickFromTable(ds.heroes[role])
        if selectedHero == -1:
            self.selectRole(role)
        return selectedHero



if __name__ == "__main__":
    menu = Menu()
    menu.userMenu()


