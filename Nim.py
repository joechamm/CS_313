#  File: Nim.py

#  Description: Gives the winning move for the game of Nim.

#  Student's Name: Joseph Cunningham

#  Student's UT EID: jsc2539
 
#  Course Name: CS 313E 

#  Unique Number: 53330

#  Date Created: 23 Jan 2011

#  Date Last Modified: 27 Jan 2011

import string 

#  With the string input line, containing the number of counters in each pile, the list
#  heaps is created by using the space between numbers as the delimiter in the split command. The total
#  xor value of all the piles is initialized to 0 as nimSumX.

def nim(line):
    heaps = line.split(' ')
    nimSumX = 0

#  The for loop computes to total xor value of all the piles, while populating heapDict with the number of counters acting as the keys.
    
    heapDict = {}
    for checks in heaps:
        nimSumX = int(checks) ^ nimSumX
        heapDict[checks] = int(checks)

#  If the total xor value of all the piles is zero, the first player will lose and there is no need to process this game any further.
#  If the total xor value is not 0, the xor value of the individual piles (which are the keys in the dictionary) are calculated and assigned
#  as the value of that key. Finally the individual pile xor values are checked against the size of the individual pile, until a pile is found
#  from which enough counters can be take to leave exactly the individual nim-sum, creating a total nim-sum of 0 and making it impossible for player 2 to win.

    if nimSumX == 0:
        print 'You Lose.'
    else:
        for checks in heaps:
            heapDict[checks] = heapDict[checks] ^ nimSumX
            if (heapDict[checks] < int(checks)):
                idx = heaps.index(checks) + 1
                heaps[(idx - 1)] = int(checks) - (int(checks) - heapDict[checks])
                print 'Remove %d counters from pile %d.' % ((int(checks) - heapDict[checks], idx))
                break
                  
def main():

##  Open the text file detailing the number and size of the piles.

    inFile = open('nim.txt', 'r')

##  Initialize switch, to process the first line detailing the number of games to be played.
    
    switch = 1

##  Going line by line through the text file, after learning the number of games to be played from the first line
##  the switch is turned off to proceed to processing the games by calling the function nim to act on the current line.
    
    gameNum = 1
    for line in inFile:
        line = line.rstrip('\n')
        if switch == 1:
            numSets = int(line)
            print 'There will be %d games.' % (numSets)
            switch = 0
        else:
            print 'Game ', gameNum
            gameNum = gameNum + 1
            nim(line)
           
    inFile.close()
main()
