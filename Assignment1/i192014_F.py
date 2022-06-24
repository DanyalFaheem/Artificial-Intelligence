# %% [markdown]
# Question 1

# %% [markdown]
# Part A

# %%
bookings = [[1,5], [3,8], [7, 10], [11, 15]]
# Making a list of cars to keep track
cars = [bookings[0]]
counter = 0
for book in bookings:
    for car in cars:
        # If car has is free during booking time, then don't add else add
        if book[0] > car[0] and book[0] < car[0] and book[1] > car[1] and book[1] < car[1]:
            counter += 0
        else:
            if book in cars:
                counter += 0
            else:
                counter += 1
                cars.append(book)
print("The number of cars required are: ", counter)

# %% [markdown]
# Part B

# %%
def most_frequent_elements_in_lis(elem_list, left, right, frequency):
    # Make two lists to keep track
    digits = [] 
    freq = []
    for i in range(left, right):
        # Add 1 to frequency list for each appended
        if elem_list[i] in digits:
            freq[digits.index(elem_list[i])] += 1
        else:
        # Append to list if not seen before
            digits.append(elem_list[i])
            freq.append(1)
    freq_elements = []
    for i in range(len(digits)):
        # Only return elements with a frequence greater than threshold
        if freq[i] >= frequency:
            freq_elements.append(digits)
    return freq_elements

lis = [2,2,4,2,4,5,6,1,1]
print(most_frequent_elements_in_lis(lis,0,5,2) )

# %% [markdown]
# Part C (i)

# %%
Assessments = [{
'roll_no': 'p18-1001', 
'marks': {
'english': (1.4, 2.5, 15, 9.6, 33),
'calculus': (2.4, 1.5, 12, 1.6, 21),
}, 'attendance': 88.4
},
{'roll_no': 'p18-1002', 
'marks': {
'english': (2.4, 1.5, 12, 1.6, 21),
'programming fundaments': (2.4, 1.5, 12, 1.6, 21),
}, 'attendance': 79.4
},
{'roll_no': 'p18-1003', 
'marks': {
'calculus': (2.4, 1.5, 12, None, 21),
'programming fundamentals': (2.4, 1.5, 12, 1.6, 21),
}, 'attendance': 79.4 }]

def get_student_marks(assessments):
    marks = {}
    for asses in assessments:
        mark = asses["marks"]
        # Create empty dictionary
        student = {}
        for m in mark:
            # Sum up the marks removing None from lists
            student[m] = sum(filter(None, list(mark[m])))
        #Add newly created student dictionary to the marks dictionary
        marks[asses["roll_no"]] = student
    return marks
    
print(get_student_marks(Assessments))


# %% [markdown]
# Part C (ii)

# %%
def get_grade(marks, policy):
    for p in policy:
        # If marks are above the threshold, return that marks
        if marks >= policy[p]:
            return p
    # If entire list traversed, then F grade it is
    return 'F'

pol = {'A': 80, 'B': 70, 'C': 60, 'D': 50}
print(get_grade(49, pol))

# %% [markdown]
# Question 2

# %% [markdown]
# Part A

# %% [markdown]
# Part (i)

# %%
#Importing numpy as gonna be required later on
import numpy as np
def second_Max_RowSum(mat):
    #Definiing default values
    highest = -100000
    secondHighest = -100000
    for arr in mat:
        # If highest changes then update secondHighest too
        if np.sum(arr) > highest:
            secondHighest = highest
            highest = np.sum(arr)
        elif np.sum(arr) > secondHighest:
            # If only second highest Changes
            secondHighest = np.sum(arr)
    return secondHighest

#Making random matrix
matrix = np.random.randint(1,10,size = (7,7) )
print("Second Highest:", second_Max_RowSum(matrix))

# %% [markdown]
# Part (ii)

# %%
def isUpperorLower(mat):
    check = True
    # Traversing the Upper triangular Matrix to make sure no value is 0
    for i in range(len(mat)):
        for j in range(i + 1, len(mat)):
            if j < len(mat):
                if mat[i][j] != 0:
                    check = False
                    break
    if check == True:
        return "Lower Triangular Matrix"
    check = True
        # Traversing the Lower triangular Matrix to make sure no value is 0
    for i in range(1, len(mat)):
        for j in range(i):
            if j < len(mat):
                if mat[i][j] != 0:
                    check = False
                    break   
    if check == True:
        return "Upper Triangular Matrix"
    # If not a triangular matrix
    return "Not a Triangular Matrix"
# array = [[3 ,0, 0, 0],
#         [0 ,0, 0, 0],
#         [0 ,0, 9, 0],
#         [0 ,1, 0, 2]]
isUpperorLower(matrix)

# %% [markdown]
# Part (iii)

# %%
def minimumSumRow(mat):
    # Defining Default Values
    minimum = 1000000
    array = []
    for arr in mat:
        # Check if less than minimum, then replace value
        if np.sum(arr) < minimum:
            minimum = np.sum(arr)
            array = arr
    return array

minimumSumRow(matrix)

# %% [markdown]
# Part (iv)

# %%
def swap_odd_rows(mat):
    # temp = []
    # temp = mat[0]
    # mat[0] = mat[2]
    # mat[2] = temp
    # temp = mat[4]
    # mat[4] = mat[6]
    # mat[6] = temp
    # return mat
    # Swapping 1st row with 3rd and 5th row with 7th
    print(mat)
    i = 1
    while i < len(mat):
        if i % 2 == 1:
            if i + 1 < len(mat) and i - 1 >= 0:
                # Swapping rows
                temp = np.copy(mat[i - 1])
                mat[i - 1] = mat[i + 1]
                mat[i + 1] = temp
            i += 4
    return mat


matrix1 = np.random.randint(1,10,size = (5,5) )
print(swap_odd_rows(matrix1))

# %% [markdown]
# Part (v)

# %%
def meanOfRows(mat):
    mean = []
    for row in mat:
        # Calculating mean and appending to list
        mean.append(int(np.sum(row) / len(row)))
    return mean

print(meanOfRows(matrix))

# %% [markdown]
# Part (vi)

# %%
def sortColumns(mat):
    # Taking transpose of matrix for columns to become rows now
    copy = mat.T
    counter = 0
    for row in copy:
        # As rows are our columns, just sorting them
        copy[counter] = np.sort(row)
        counter += 1
    # Returning the transpose to change rows back to columns
    return copy.T
print(sortColumns(matrix))    

# %% [markdown]
# Part B

# %%
def charMatrix(mat, str):
    j = 0
    for i in range(len(str)):
        # Updating to start of matrix if N reached
        if j >= (len(mat)):
            j = 0
        # If a character already discovered, then change value to - so it can't be used again
        if str[i] in mat[j]:
            x = mat[j].where(str[i])
            mat[j][x] = '-'
        else:
            return 'No'
    return 'Yes'

        

# %% [markdown]
# Part C

# %%
def hourglass(mat):
    # Defining default values
    sum = -10000000
    array = []
    for i in range(0,4):
        array1 = []
        for j in range(0,4):
            # Getting our hourglass values, adding 0 for padding
            array1 = [mat[i][j], mat[i][j + 1], mat[i][j + 2], 0, mat[i + 1][j + 1], 0, mat[i + 2][j], mat[i + 2][j + 1], mat[i + 2][j + 2]]
            if np.sum(array1) > sum:
            # Update values if sum is greater and keep value of new hourglass
                sum = np.sum(array1)
                array = array1
    print("The maximum sum of hourglass is:", sum)
    print("The hourglass with maximum sum is:", array)

hourglass(matrix)

# %% [markdown]
# Part D

# %% [markdown]
# Part (i)

# %%
def replaceArr(arr):
    # Using the builtin function to just check mod values
    arr[arr % 2 == 1] = -1
    print(arr)

replaceArr(np.array([3, 6, 7, 0, 7, 0, 4, 9, 8]))

# %% [markdown]
# Part (ii)

# %%
def getArray(arr):
    # Making temp list in function
    copy = []
    for a in arr:
        # Checking conditions
        if a <= 10 and a >= 5:
            copy.append(a)
    return copy

# Making random size array every time
getArray(np.random.randint(1,17,size = (np.random.randint(1,17,size = (1)))))

# %% [markdown]
# Question 3

# %% [markdown]
# Part A

# %%
def anagram(str1, str2):
    # Checking first condition of size of each string
    if len(str1) != len(str2) or str1 == str2:
        return False
    for i in range(len(str1)):
        # If character is present in other string, then moving on
        if str1[i] in str2:
            continue
        else:
            return False
    # If all characters are present then true
    return True

anagram("abc", "acb")

# %% [markdown]
# Part B

# %%
def rotation(str1, str2):
    # Checking first condition of size of each string
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        # If character is present in other string and not at the same location, then moving on
        if str1[i] in str2 and str1[i] != str2[i]:
            continue
        else:
            return False
    return True

rotation("XYZ", "YXZ")

# %% [markdown]
# Part C

# %%
def superString(str):
    alphabet = {}
    char = 'Z'
    # Creating our new dictionary of alphabets
    for i in range (1, 27):
        alphabet[char] = i
        char = chr(ord(char) - 1)
    for s in str:
        # Checking count of char in string according to dictionary value
        if str.count(s) == alphabet[s]:
            continue
        else:
            return False
    return True

superString("ZYYZ")

# %% [markdown]
# Part D

# %%
def substringPalindrome(str):
    # Creating a new set here
    sets = set()
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            # Creating substrings of each possible size and characters
            str1 = str[i:j]
            # Checking for palindrome by checking reverse string equal to original string
            if str1[::-1] == str1:
                # If palindrome, add to set, set will automatically discard duplicate values, thus no need to check for uniqueness
                sets.add(str1)
    return sets

substringPalindrome("ABBA")

# %% [markdown]
# Question 4

# %%
# Importing our libraries for use at start
import random
import copy

# Class of Card, each card represents one card in the Deck
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    # Defining representation for easy output
    def __repr__(self):
        return str(self.suit) + ":" + str(self.rank)
    # Our relevant getter setters
    def getSuit(self):
        return self.suit
    def getRank(self):
        return self.rank
    def setSuit(self, suit):
        self.suit = suit
    def setRank(self, rank):
        self.rank = rank

# Class Deck which would be our start Deck and Discard Pile later on
class Deck():
    # Our list of cards
    cards = []

    def __init__(self):
        # Initializing our deck with the original 52 cards
        dict = [1, 2, 3, 4, 5, 6, 7, 8, 9, "Jack", "Queen", "King", "Ace"]
        for i in range(0, 53):
            if int(i / 13) == 0:
                self.cards.append(Card("Spade", dict[i % 13]))
            elif int(i / 13) == 1:
                self.cards.append(Card("Heart", dict[i % 13]))
            elif int(i / 13) == 2:
                self.cards.append(Card("Clove", dict[i % 13]))
            elif int(i / 13) == 3:
                self.cards.append(Card("Diamond", dict[i % 13]))
    
    # Defining representation for easy output
    def __repr__(self):
        return str(self.cards)

    # Shuffle function to shuffle our deck
    def shuffle(self):
        random.shuffle(self.cards)

    # Defining own find and Delete functions for our deck
    def find(self, card):
        return self.cards.index(card)

    def delete(self, card):
        del self.cards[self.find(card)]
    # Function to cut the deck randomly
    def cutDeck(self):
        # self.cards = self.cards[random.randint(1, int(len(self.cards) / 2))]
        self.shuffle()

# Our player class for each Player
class Player():
    # Cards list for each Player
    cards = []

    def __init__(self, cards=0):
        self.cards = cards
    # Defining representation for easy output
    def __repr__(self):
        return str(self.cards)
    # Relevant getter setters
    def getCards(self):
        return self.cards
    
    def setCards(self, cards):
        self.cards = cards

# Our Main Driver Class
class Game():
    # Main Players list
    Players = []
    # Main Deck Object that is our discard pile later on
    Deck = Deck()
    def __init__(self):
        playerCards = []
        # Shuffling our deck before distributing cards
        self.Deck.shuffle()
        for i in range(int(input("Enter number of players: \n"))):
            playerCards = []
            # Distributing original 5 cards to each player
            for j in range(5):
                index = random.randint(0, len(self.Deck.cards))
                playerCards.append(copy.deepcopy(self.Deck.cards[index]))
                self.Deck.delete(self.Deck.cards[index])
            self.Players.append(Player(playerCards))
            # Cutting our deck after distributing cards
            self.Deck.cutDeck()
        print(self.Players, len(self.Deck.cards))
    
    # Our main driver function that will run in the game
    def playGame(self):
        gameOver = False
        while gameOver != True:
            # Traversing player by player
            for player in self.Players:
                card = self.Deck.cards[0]
                playerDeck = player.getCards()
                # Asking the player for his choice
                print("The card at top is:" ,card)
                print("It is turn of player", self.Players.index(player) + 1)
                print("Your current cards are", playerDeck)
                # Getting input here
                inp = int(input("Which card would you like to play? Enter between 1 and " + str(len(playerDeck)) + "\n Enter 0 to pass"))
                # If player wants to pass his turn
                if inp == 0:
                    continue
                # Checking if same suits
                elif card.getSuit() != playerDeck[inp - 1].getSuit():  
                    print("Invalid card. Please follow the Rules!")
                
                elif isinstance(playerDeck[inp - 1].getCard(), int) and isinstance(card.getRank(), int):
                    # Checking if the same suit but in order ranks
                    if int(card.getRank()) != 1 + int(playerDeck[inp - 1].getRank()):
                        print("Invalid card. Please follow the Rules!")
                    # If In order ranks, update cards accordingly
                    elif int(playerDeck[inp - 1].getRank()) <= 4 and int(playerDeck[inp - 1].getRank()) >= 2:
                        for i in range(0, int(playerDeck[inp - 1].getRank())):
                            self.Players[self.Players.index(player) + 1].getCards().append(copy.deepcopy(self.Deck.getCards[i]))
                            self.Deck.delete(self.Deck.cards[i])
                print(playerDeck)
            break
        

# Start the game here
G = Game()
G.playGame()

# %%


# %%



