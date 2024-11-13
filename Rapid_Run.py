import random as r
import time as t

horse = []      # All the records of each horse collectively

hId = []        # All the records of each horse ids in a list
hName = []      # All the records of each horse names in a list
hJockey = []    # All the records of each horse jockeys in a list
hAge = []       # All the records of each horse ages in a list
hBreed = []     # All the records of each horse breeds in a list
hWin = []       # All the records of each horse total wins in a list
hRace = []      # All the records of each horse total races in a list
hGroup = []     # All the records of each horse's group in a list

GroupA = []
GroupB = []
GroupC = []
GroupD = []

rando = []      # random horse selected from each group for the race (as in indexes of horse ids)
time = []       # randomly select time durations for four horses and order it in ascending
podium = []     # slice the time as to only get the first 3 element
podiumWinners = []
results = {}

race = False


def initialization():

    with open('Horse.txt') as f:            # Open the 'Horse.txt' file and read all lines
        lines = f.readlines()

        for line in lines:                  # Remove any whitespace, parse each line, then divide each section with a comma to obtain a list of the horse's information
            horse.append(line.strip().split(','))
        # print(horse)

    for k in range(len(horse)):             # Repeat over every horse record that has been parsed, extracting relevant information and append to it's appropriate list

        m = 0
        hId.append(int(horse[k][m]))

        m += 1
        hName.append(horse[k][m])

        m += 1
        hJockey.append(horse[k][m])

        m += 1
        hAge.append(int(horse[k][m]))

        m += 1
        hBreed.append(horse[k][m])

        m += 1
        hWin.append(int(horse[k][m]))

        m += 1
        hRace.append((horse[k][m]))

        m += 1
        hGroup.append(horse[k][m])

    SHDcopy()
    print()


def test():
    print("Horse ID :", hId)
    print("Horse Name :", hName)
    print("Horse Jockey :", hJockey)
    print("Horse Age :", hAge)
    print("Horse Breed :", hBreed)
    print("Horse Win :", hWin)
    print("Horse Race :", hRace)
    print("Horse Group :", hGroup)


def validInput(display, data_type):

    while True:

        try:
            Input = input(display)          # Ask the user for input
            return data_type(Input)         # Converting the user-provided input to the specified data type.


        except ValueError:          # If a ValueError occurs during conversion, catch it and print an error message
            print(f"Invalid input. Please enter a valid {data_type.__name__}.")
            # __name__ is an attribute that returns the name of the class or type as a string <data_type>


def onlyLetters(display):

    while True:

        try:
            Input = input(display)          # Ask the user for input
            if not Input.isalpha():         # Check if the input contains only letters
                raise ValueError("Input must contain only letters.")        # Raise a ValueError if the input contains non-letter characters
            return Input                    # Return the valid input if it passes the conditions

        except ValueError as ve:
            print(f"Error: {ve}")           # Display the ValueError by printing an error message
            continue


def onlyABCD(display):
    valid_letters = {'A', 'B', 'C', 'D'}         # Define the proper letter set {A,B,C,D}

    while True:

        try:
            Input = input(display).upper()  # Convert input to uppercase for case-insensitivity
            if Input not in valid_letters:  # Check if the input is not in the set letters
                raise ValueError("Input must be one of: {A, B, C, D}.")     # Raise a ValueError if the input is not the set
            return Input    # Return the valid input if it passes the conditions

        except ValueError as ve:
            print(f"Error: {ve}")   # Display the ValueError by printing an error message
            continue


def checkDuplication(input, list):
    return input in list            # Check if the input is in respective list and return True/False

def SHDcopy():
    # Implement sorting algorithm
    for i in range(len(horse)):
        min = i
        for j in range(i + 1, len(horse)):
            if int(horse[j][0]) < int(horse[min][0]):
                min = j

        # Swap the found minimum element with the first element
        horse[i], horse[min] = horse[min], horse[i]

    print(horse)
    # Save the sorted horse details to the 'Horse_Detail.txt' file
    with open('Horse_Detail.txt', 'w') as f:
        comma = ','         # Define a comma as the end part for joining elements
        for record in horse:            # Iterate through each record in the 'horse' list
            f.write(comma.join(map(str, record)) + '\n')        # Write the record as a comma-separated string to the file, followed by a newline character

    print(f'Save Successful\n')


def AHD():
    while len(hId)<20:
        print('\nPlease Add Accordingly _')

        horseid = validInput('Horse ID: ', int)                                  # Get a valid horse id from the user

        while checkDuplication(horseid, hId):                                               # Check for duplication if True
            print("Error: Horse ID already exists. Please choose a different one.")         # Display Error
            horseid = validInput('Horse ID: ', int)                                 # Ask the user to input again

        horsename = onlyLetters('Horse\'s Name: ')                                      # Get a valid horse name from the user

        while checkDuplication(horsename, hName):                                               # Check for duplication if True
            print("Error: Horse's Name already exists. Please enter a different one.")          # Display Error
            horsename = onlyLetters('Horse\'s Name: ')                                          # Ask the user to input again

        horsejockey = onlyLetters('Horse Jockey\'s Name: ')                             # Get a valid horse jockey from the user

        while checkDuplication(horsejockey, hJockey):                                               # Check for duplication if True
            print("Error: Horse Jockey's Name already exists. Please enter a different one.")       # Display Error
            horsejockey = onlyLetters('Horse Jockey\'s Name: ')                                     # Ask the user to input again

        hId.append(horseid)                                                             # append valid and unique inputs to respective lists
        hName.append(horsename)                                                         # append valid and unique inputs to respective lists
        hJockey.append(horsejockey)                                                     # append valid and unique inputs to respective lists
        hAge.append(validInput('Horse\'s Age: ', int))                          # Get a valid horse age from the user and append to respective list
        hBreed.append(onlyLetters('Horse Breed: '))                                    # Get a valid horse breed from the user and append to respective list
        hWin.append(validInput('Wins Horse got from participating: ', int))     # Get a valid number of wins horse got from race, from the user and append to respective list
        hRace.append(validInput('Total races Horse participated: ', int))       # Get a valid total number of races horse ran, from the user and append to respective list
        hGroup.append(onlyABCD('Horse Group [A/B/C/D] : '))                             # Get a valid horse group from the user and append to respective list

        # append last element from each list in order as to save a horse detail in one list
        horse.append([hId[-1], hName[-1], hJockey[-1], hAge[-1], hBreed[-1], hWin[-1], hRace[-1], hGroup[-1]])

        print()
        test()

        SHDcopy()       # save the alteration in temporarily value holding text file
        break
    else:
        print("You have exceeded the horse limit. Please delete a horse to add")

def delete(a):      # Remove the element at index 'a' from each list
    hId.pop(a)
    hName.pop(a)
    hJockey.pop(a)
    hAge.pop(a)
    hBreed.pop(a)
    hRace.pop(a)
    hWin.pop(a)
    hGroup.pop(a)
    horse.pop(a)


def update(a):
    # Display instructions for updating horse details
    print(f'-  Type the Letter Corresponding to the word')
    print(f'-  I:ID | N:Name | J:Jockey | A:Age | B:Breed | R: TOTAL RACE | W: RACES WON | G: GROUP\n')

    while True:                                                                             # Continue displaying the user until a valid update choice is made
        ans = onlyLetters('- What do you what do update regrading this horse : ').upper()   # Get user's choice for what to update

        match ans:                                                                          # Use a match statement to handle different update cases
            case "I":
                tempID = validInput('Enter what you want to replace as: ', int)     # Get a valid horse id from the user

                while checkDuplication(tempID, hId):                                            # Check for duplication till unique value is inputed
                    print("Error: Horse ID already exists. Please choose a different one.")
                    tempID = validInput('Horse ID: ', int)
                hId[a] = tempID                                                                 # update horse id
                break

            case "N":
                hName[a] = onlyLetters('Enter what you want to replace as: ')               # Get a valid horse name and update
                break

            case "J":
                hJockey[a] = onlyLetters('Enter what you want to replace as: ')              # Get a valid horse jockey and update
                break

            case "A":
                hAge[a] = validInput('Enter what you want to replace as: ', int)     # Get a valid horse age and update
                break

            case "B":
                hBreed[a] = onlyLetters('Enter what you want to replace as: ')               # Get a valid horse breed and update
                break

            case "R":
                hRace[a] = validInput('Enter what you want to replace as: ', int)      # Get a valid number of wins horse got from race and update
                break

            case "W":
                hWin[a] = validInput('Enter what you want to replace as: ', int)      # Get a valid number of wins horse got from race and update
                break

            case "G":
                hGroup[a] = onlyLetters('Enter what you want to replace as: ')  # Get a valid horse group and update
                break

            case _:                                                                     # for other Any invalid match
                print("Try again. Enter the corresponding letter")
                continue

    test()


def DHD():
    hId2 = validInput(f'-   ENTER THE "Horse ID" OF THE HORSE\'S RECORD TO DELETE : ', int)         # Get a valid horse id from the user
    j = hId.index(hId2)                 # Get the index of specific horse id
    delete(j)                           # Call function to pop the elements in all list of respective index of horse id

    SHDcopy()                           # save the alteration in temporarily value holding text file


def UHD():
    hId3 = validInput(f'-   ENTER THE "Horse ID" OF THE HORSE\'S RECORD TO UPDATE : ', int)         # Get a valid horse id from the user
    j = hId.index(hId3)                 # Get the index of specific horse id

    update(j)                           # Call function to update the element for the provide list as per the respective index of the horse id
    horse.clear()                       # Delete all elements in where all horse details are saved

    for i in range(len(hId)):
        horse.append([hId[i], hName[i], hJockey[i], hAge[i], hBreed[i], hWin[i], hRace[i], hGroup[i]])

    SHDcopy()                                       # save the alteration in temporarily value holding text file


def VHD():
    # Define header
    header = "| horseId |        horseName        |        horseJockey         | horseAge |      horseBreed      | totalWin | totalRace | horseGroup |"

    # Print the header
    print('-' * 136)
    print(header)
    print('-' * 136)

    # Read data from the file
    with open('Horse_Detail.txt') as f:
        lines = f.readlines()

    # Print data as a table
    for line in lines:
        # Split the line into individual values
        data = line.strip().split(',')

        # Format and print each value
        print(
            f"| {data[0]:<7} | {data[1]:<23} | {data[2]:<26} | {data[3]:<8} | {data[4]:<20} | {data[5]:<8} | {data[6]:<9} | {data[7]:10} |")
        print('-' * 136)
    print()
    t.sleep(5)


def SHD():
    print(f'\n- YOU ARE GOING TO SAVE CHANGES YOU MADE')                # Prompt the user to confirm saving changes
    y_n = input("- To conform Type : 'Y'/'y'  | if you have second thoughts Type : 'N'/'n'\n    TYPE YOUR OPTION : ")

    while True:             # Continue prompting until a valid option is chosen
        match y_n:
            case 'Y' | 'y':
                with open('Horse.txt', 'w') as f:
                    comma = ','
                    for record in horse:
                        f.write(comma.join(map(str, record)) + '\n')

                # Notify the user that the save was successful
                print('\nSave Successful')
                break

            case 'N' | 'n':
                print('\nOkay!')        # Notify the user that changes will not be saved
                break

            case _:
                print("invalid option!")        # Handle invalid input
                continue

def SDD():
    global rando
    total_index = len(hId)      # Get the total number of horses

    for n in range(total_index):             # Repeat through all horses to categorize them into groups
        group = hGroup[int(n) - 1]           # Extract the group of the horse based on its index

        match group:                        # Use a match statement to categorize horses into respective groups
            case 'A':
                GroupA.append(n)

            case 'B':
                GroupB.append(n)

            case 'C':
                GroupC.append(n)

            case 'D':
                GroupD.append(n)

    # print(GroupA)
    # print(GroupB)
    # print(GroupC)
    # print(GroupD)

    # Generate a random selection of horses, one from each group
    rando = [r.choice(GroupA), r.choice(GroupB), r.choice(GroupC), r.choice(GroupD)]

    print(rando)
    print()

    # Display the details of the randomly selected horses
    for i in rando:
        print(horse[i - 1])


def WHD(a):
    # Declare global variables for broader scope
    global results
    global time
    global podium
    global podiumWinners
    print()
    # print(a)

    # Define the time that will be accessed by the horses when they run their race
    time_slot = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    # Randomly sample 4 times for the horses to race
    time = r.sample(time_slot, 4)

    results = {time[0]: a[0], time[1]: a[1], time[2]: a[2], time[3]: a[3]}

    print(time)
    print(results)

    print(results.get(time[0]))
    print(results.get(time[1]))
    print(results.get(time[2]))
    print(results.get(time[3]))
    # Sort the time slots in ascending order
    time = sorted(time)
    # Select the top 3 time slots as the podium
    podium = time[:3]

    # Get the horse IDs for the first, second, and third places
    first = int(results.get(podium[0]))
    second = int(results.get(podium[1]))
    third = int(results.get(podium[2]))
    # Store the podium winners in a list
    podiumWinners = [first, second, third]
    print(podiumWinners)
    # Display a message indicating that the race is running and show the podium
    print(f'\n\n------ Race is running ------\n\n')
    t.sleep(5)
    print(f'THE THIRD PLACE :\n{horse[third - 1]}\n')
    t.sleep(1)
    print(f'THE SECOND PLACE :\n{horse[second - 1]}\n')
    t.sleep(2)
    print(f'THE FIRST PLACE :\n{horse[first - 1]}\n')
    t.sleep(3)
    print()


def VWH():
    # Declare global variables for broader scope
    global podium
    global podiumWinners
    # Create empty lists to store horse names of winners and conversation of time to star print
    Names = []
    podiumTime = []

    for i in podium:                        # Convert time to star values as per to visualize
        i = int(i / 10)
        podiumTime.append(i)                # Add the star time

    print(hId)
    print(podiumWinners)

    # Append the Names list with the names of horses in the podium
    for i in podiumWinners:
        Names.append(hName[i-1])

    placing = ['first', 'second', 'third']

    # Print the final race results with horse names, podium times, and placing labels
    for i in range(len(podium)):
        print(f'{placing[i]} place : {Names[i]} {podiumTime[i] * "*":<11} ({podium[i]}s)')


def main_menu():
    global race     # Declare global variable for race status

    while True:
        # Get user input for menu options
        Input = str(input(
            '''\n       ---- Main MENU INFO ----\n\n
-   AHD to Adding horse details
-   DHD to Deleting horse details
-   UHD to Updating horse details
-   VHD to View horse details
-   SHD to Save horse details   (Note that this function must be used at the end, after altering horse details)
-   SDD to Select random horses and start race
-   WHD to View horse details
-   VWH to Visualize Won horse details
-   ESC to QUIT         \n
    TYPE YOUR OPTION : '''))

        # Convert user input to uppercase
        Input = Input.upper()
        # Use match statement to handle different menu options
        match Input:                # Set race to True if user selects 'WHD' or 'VWH'
            case 'WHD' | 'VWH':
                race = True
        # Check if race is not active and execute corresponding functions
        match Input:
            case 'AHD' if not race:
                AHD()

            case 'DHD' if not race:
                DHD()

            case 'UHD' if not race:
                UHD()

            case 'VHD' if not race:
                VHD()

            case 'SHD' if not race:
                SHD()

            case 'SDD' if not race:
                SDD()
                race = True
            # Check if race is active and execute corresponding functions
            case 'WHD' if race:
                WHD(rando)

            case 'VWH' if race:
                VWH()
                race = False
            # Exit the main menu loop if user enters 'ESC'
            case 'ESC':
                break
            # Handle invalid options
            case _:
                print(f'\n++ INVALID OPTION. Enter Options accordingly ++\n')
                pass


initialization()
test()
main_menu()

