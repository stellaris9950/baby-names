# BABY NAMES DATA ASSIGNMENT START CODE

import json


def main():
    # Load Baby Data from File
    file = open("baby-names-data.json")
    baby_data = json.load(file)
    file.close()
    # Main Menu
    loop = True
    while loop:
        selection = getMenuSelection()

        if selection == "1":
            displayAll(baby_data)
        elif selection == "2":
            searchGender(baby_data)
        elif selection == "3":
            searchRank(baby_data)
        elif selection == "4":
            searchStartLetter(baby_data)
        elif selection == "5":
            searchNameLength(baby_data)
        elif selection == "6":
            print("\nGOODBYE!\n")
            loop = False


def getMenuSelection():
    # Print Menu & Return User Selection
    print("\n*** BABY DATA - MAIN MENU ***"
          "\n* 1: Display All"
          "\n* 2: Search by Gender"
          "\n* 3: Search by Rank"
          "\n* 4: Search by Starting Letter"
          "\n* 5: Search by Name Length"
          "\n* 6: Exit")

    return input("* Enter Option #: ")


def displayAll(baby_data):
    # Display All Baby Data
    for baby in baby_data:
        print(f"{baby['name']} (Rank {baby['rank']}, Gender: {baby['gender']})")

def searchGender(baby_data):
    # Dislay All Baby Names based on Gender
    later_list = []
    for baby in baby_data:
        if baby['gender'] == "Girl":
            print(f"{baby['name']} (Rank {baby['rank']}, Gender: {baby['gender']})")
        else:
            later_list.append(baby)
    for baby in later_list:
        print(f"{baby['name']} (Rank {baby['rank']}, Gender: {baby['gender']})")
def searchRank(baby_data):
    # Display All Baby Names based on Rank
    print("\nSEARCH BY RANK")


def searchStartLetter(baby_data):
    # Insert User Item into a Position
    print("\nSEARCH BY START LETTER")


def searchNameLength(baby_data):
    # Remove item from position
    print("\nSEARCH BY NAME LENGTH")
# Invoke main to begin program


main()
