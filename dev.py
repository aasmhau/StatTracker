import os
import time
import msvcrt
from data import DataStructures as ds


class Menu:

    def selectOptionFromTable(self, choiceList: list) -> int:
        os.system('cls')
        asciiInt = 97
        optionList = []

        # Make sure input is only ascii (char.isalpha())
        for option in choiceList:
            print("{}  -  {}".format(chr(asciiInt), option))
            optionList.append(option)
            asciiInt += 1

        selection = int(ord(msvcrt.getch())) - 97
        while(selection < 0 or selection > len(optionList)-1):
            selection = int(ord(msvcrt.getch())) - 97
        return optionList[selection] 

    def userMenu(self):
        menuOptions = ['Register Match', 'Exit'] 
        while(True):
            menuSelection = self.selectOptionFromTable(menuOptions)

            match menuSelection:
                case 'Register Match':
                    self.registerMatch()
                case 'Exit':
                    print("Thank you for using this program!")
                    break

    def registerMatch(self):
            selectedMode = self.selectOptionFromTable(ds.maps)
            selectedMap = self.selectOptionFromTable(ds.maps[selectedMode])
            selectedRole = self.selectOptionFromTable(ds.heroes)
            selectedHero = self.selectOptionFromTable(ds.heroes[selectedRole])
            selectedResult = self.selectOptionFromTable(ds.results)

            print("Written to output.txt: {} | {} | {} | {} | {}".format(selectedMode, selectedMap, selectedRole, selectedHero, selectedResult))
            time.sleep(3)

    def writeToFile(self):
        pass
        # Add current date and time to input string


if __name__ == "__main__":
    menu = Menu()
    menu.userMenu()


