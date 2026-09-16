import random
import datetime


def main(): #main function that calls all other functions
    print("☃️Welcome to Snowman☃️")
    initials = str(input("Enter the first 3 letters of your name: ")).upper()

    while len(initials) <= 1 or len(initials) > 3:
        initials = input("Enter your initials (1–3 characters): ")

    option = 0

    scoreLst = loadScoreboard()
    wordLst = loadWords()  #words stored in this list
    catLst = loadCategories()
    while option != 4:
        option = menu()
        if option == 1:
           score = playGame(wordLst, catLst)
           writeScoreboard(scoreLst,initials,score) #writes to file new scores




        elif option == 2:
            showScoreboard(scoreLst) # this should print the updated scoreboard lst variable
        elif option == 3:
            addWord(catLst,wordLst)
        elif option == 4:
            print("Thank you for playing")
        else:
            print("Invalid option")



def sortscorefn(scorelst):
    value = scorelst[1]
    return int(value)

def showScoreboard(scoreLst):
    print("🏆 Scoreboard 🏆")
    scoreLst.sort(key=sortscorefn, reverse=True)
    for row in scoreLst:
        print(row,end = "\n")







def writeScoreboard(scoreLst, initials, score):
    dt = datetime.datetime.now()
    dt = dt.strftime("%d/%m/%Y %H:%M")

    found = False
    for row in scoreLst:
        if row[0] == initials.upper():
            row[1] = int(row[1])
            row[1] += score
            row[2] = dt
            row[1] = str(row[1])
            found = True
    if found == False:
        newperson = [initials, score, dt]
        scoreLst.append(newperson)
    file = open("Scoreboard.txt", "w")
    for row in scoreLst:
        file.write(str(row[0])+","+str(row[1])+","+str(row[2])+"\n")
    file.close()











def loadScoreboard():
    try:
        fileObj = open("Scoreboard.txt", "r")
        scoreLst = []

        for line in fileObj:
            line = line.rstrip("\n")
            lineLst = line.split(",")
            scoreLst.append(lineLst)
        fileObj.close()
        return scoreLst
    except FileNotFoundError as error:
        print(error)
        print("File not found")






def loadWords(): #stores words.txt into the wordLST
    try:
        fileObj = open("Words.txt", "r")
        wordLst = []

        for line in fileObj:
            line = line.rstrip("\n")
            lineLst = line.split(",")

            wordLst.append(lineLst)
        fileObj.close()
        return wordLst

    except FileNotFoundError as error:
        print(error)
        print("File not found")


def loadCategories(): #loads the categories into the catLst
    try:
        fileObj = open("Categories.txt", "r")
        catLst = []


        for line in fileObj:
            line = line.rstrip("\n")
            catLst.append(line)
        fileObj.close()
        return catLst
    except FileNotFoundError as error:
        print(error)
        print("File not found")


def addWord(catLst,wordLst):
    print("Add New Word")
    try:
        word = input("Enter the word: ")
        while word in wordLst:
            print("Word already exists")

        # Category
        print("Categories: animal, state, europe")
        category = input("Enter category: ").lower()

        while category not in catLst:
            category = input("Invalid category. Enter again: ").lower()

        # Difficulty
        print("Difficulty: easy, medium, hard")
        difficulty = input("Enter difficulty: ").lower()

        while difficulty not in ["easy", "medium", "hard"]:
            difficulty = input("Invalid difficulty. Enter again: ").lower()


        file = open("Words.txt", "a")
        file.write(category + "," + difficulty + "," + word + "\n")
        file.close()
    except FileNotFoundError as error:
        print(error)
        print("File not found")

    print("✅ Word added successfully!")



def menu(): #menu for picking options
    print("1) Play The Game☃️")
    print("2) Show Scoreboard🏆")
    print("3) Manage Game⚙️")
    print("4) Exit👋")

    try:
        option = int(input("Pick any option: "))
        return option
    except ValueError:
        print("Please enter a number not a letter.\n")


def playGame(wordLst,catLst):#playGame function
    print (catLst)

    category = input("Enter the category of the game: ")
    category = category.lower()
    if category not in catLst:
       category = input("Invalid category. Enter again: ").lower()
    print()
    print("\t\tDifficulty ")
    print("['easy', 'medium', 'hard]")
    difficulty = input("Enter the difficulty of the game: ")
    difficulty = difficulty.lower()
    if difficulty not in ("easy", "medium", "hard"):
        difficulty = input("Invalid difficulty. Enter again: ").lower()

    shortLst = []

    for row in wordLst:
        if row[0] == category and row[1] == difficulty:
            shortLst.append(row[2])

    print("Found",len(shortLst),"words")

    rnd = random.randint(0, len(shortLst) - 1)  # picks the random word



    selectedWord = shortLst[rnd]
    selectedWordLst = list(selectedWord)

    maskedWord = len(selectedWord) * "?"
    maskedWordLst = list(maskedWord)






    lives = 5
    score = 0

    while lives != 0:
        print("You have",lives,"lives to guess the word GoodLuck!!")
        print(maskedWord)
        guess = input("Guess a letter of the word: ")


        if guess in selectedWordLst:
            index = selectedWord.find(guess)

            maskedWordLst[index] = str(guess)
            selectedWordLst[index] = "?"
            selectedWord = "".join(selectedWordLst)
            maskedWord = "".join(maskedWordLst)
            print("You guessed a letter in the word!!")
            print(maskedWord)
            print("lives: ",lives, "❄️")

            if "?" not in maskedWordLst:
                print("Well Done!! You guessed the word!!️️☃️")
                if difficulty == "easy":
                    score += 1
                elif difficulty == "medium" :
                    score += 5
                else:
                    score += 10

                break

        else:
            print("The word does not contain the letter ", guess)
            lives -= 1
            print("lives",lives,"❄️")

        if lives == 0:
            print("Game Over your out of lives unlucky😞")

    return score




main()