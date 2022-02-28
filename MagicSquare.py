##  File: MagicSquare.py
##
##  Description: Creates an n x n magic square.
##
##  Student's Name: Joseph Cunningham
##
##  Student's UT EID: jsc2539
## 
##  Course Name: CS 313E 
##
##  Unique Number: 53330
##
##  Date Created: 31 Jan 2011
##
##  Date Last Modified: 4 Feb 2011

import math
import string

##  The isMagic function checks to see if the list given as input satisfies the definition of a magic square. It first
##  puts the sum of each row into a list, then the sum of each column into a list, then puts the sum of the diagonals into a list,
##  then finally checks that these sums are all equal.

def isMagic (b):
    hSums = []
    for row in b:
      rowSum = 0
      for i in row:
        rowSum = rowSum + int(i)
      hSums.append(rowSum)

    vSums = []
    for i in range (len(b)):
      colSum = 0
      for j in range (len(b[i])):
        colSum = colSum + int(b[j][i])
      vSums.append(colSum)

    dSums = []
    dForwardSum = 0
    dBackSum = 0
    for i in range (len(b)):
      dForwardSum = dForwardSum + int(b[i][i])
    dSums.append(dForwardSum)
    for i in range ((len(b) - 1),-1,-1):
      dBackSum = dBackSum + int(b[i][i])
    dSums.append(dBackSum)
  
    if (set (hSums) == set (vSums) == set (dSums)):
        print ''
        print 'Sum of row = ', hSums[0]
        print 'Sum of column = ', vSums[0]
        print 'Sum of diagonal (UL to LR) = ', dSums[0]
        print 'Sum of diagonal (UR to LL) = ', dSums[0]        
    else:
        print 'Not a Magic Square'


##  The printSquare function will print the magic square by first determining the number of digits in the largest number and right
##  justifying every element according to this size.


def printSquare ( magicSquare ):
    size = len(magicSquare)
    lrgNum = size**2
    numDigits = int((math.log10(lrgNum))) + 2
    print 'Here is a %d x %d magic square:' % (size,size)
    print ''
    for i in range(0,size):
        for j in range(0,(size - 1)):
            print repr(magicSquare[i][j]).rjust(numDigits),
        print repr(magicSquare[i][(size - 1)]).rjust(numDigits)


## The makeSquare function will create an n x n list, then populate the list according
## to the magic square algorithm.

def makeSquare (n):

##  Start with an n x n list, where every entry is 0. This will make it possible to traverse the list, by simply checking if the
##  value of the desired entry is 0 or not. The iCoord variable will indicate the row index, and jCoord will indicate the column index.

    
    magicSquare = []
    nSquare = n**2
    iCoord = (n - 1)
    jCoord = n / 2

    for i in range(1,n+1):
        tempList = []
        for j in range(1,n+1):
            tempList.append(0)
        magicSquare.append(tempList)

##  The for loop will fill in the values from 1 to n squared, by first checking if the entry in the ith row and jth column
##  is zero, and if so entering the next value in that entry. If the entry is not zero, or the value for k has alread been entered
##  the index is increased according to the given algorithm. Once the magic square has been created, it will be printed with
##  the determination of whether or not it actually is a magic square.
        
    for k in range(1, nSquare + 1):
        if magicSquare[iCoord][jCoord] == 0:
            magicSquare[iCoord][jCoord] = k
            if (iCoord == (n - 1)) and (jCoord == (n - 1)):
                iCoord = iCoord - 1
            else:
                iCoord = (iCoord + 1) % n
                jCoord = (jCoord + 1) % n
        else:
            iCoord = (iCoord - 2) % n
            jCoord = (jCoord - 1) % n
            if magicSquare[iCoord][jCoord] == 0:
                magicSquare[iCoord][jCoord] = k
                iCoord = (iCoord + 1) % n
                jCoord = (jCoord + 1) % n            
    printSquare( magicSquare )
    isMagic( magicSquare )

def main():
    n = 2
##  Initialize n to an even number to enter the while loop, and ensure that n is odd and larger than 3.
    while (n % 2 == 0) or (n < 3):
        n = input('Enter an odd integer, 3 or greater: ')
        if (n % 2 == 0):
            print '%d is not an odd integer. Please enter an odd integer.' % (n)
        if (n < 3):
            print '% is not greater than 3. Please choose a number, greater than 3' % (n)

##  Call the makeSquare function with variable n.

    magicSquare = makeSquare(n)        
main()
