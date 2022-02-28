## File: Boxes.py
##
##  Description: Finds the largest list of nested boxes.
##
##  Student's Name: Joseph Cunningham
##
##  Student's UT EID: jsc2539
##
##  Course Name: CS 313E 
##  
##  Unique Number: 53330 
##
##  Date Created: 8 Mar 2011
##
##  Date Last Modified: 11 Mar 2011


class Queue (object):
    def __init__ (self):
        self.queue = []

    def enqueue (self, item):
        self.queue.append (item)

    def dequeue (self):
        return (self.queue.pop(0))

    def isEmpty (self):
        return (len (self.queue) == 0)

    def size (self):
        return len (self.queue)
 

class Box(object):
    def __init__(self, x, y, z):
        self.dimension = [x,y,z]
        self.dimension.sort()


##  The doesFit function returns true or false depending on if the box being acted upon nests inside the other.
##  This will only be true when the x,y,z dimensions are all strictly less than the other boxes corresponding dimensions.
##  Since the dimensions of each box were sorted upon their creation, there is no need to check if the boxes can be rotated
##  to give another nesting.

    def doesFit (self, other):
        return (self.dimension[0] < other.dimension[0] and self.dimension[1] < other.dimension[1] and self.dimension[2] < other.dimension[2])
    
    def compare(self, other):

        if self.dimension[0] < other.dimension[0]:
            return -1
        elif self.dimension[0] == other.dimension[0]:
            return 0
        else:
            return 1

##  The bubbleSort function is used to sort the list of boxes according to their smallest dimension.

def bubbleSort1 (createdBoxes):
    idx = 0
    while (idx < len(createdBoxes) - 1):
        jdx = len(createdBoxes) - 1
        while (jdx > idx):
            if (createdBoxes[jdx][1].compare(createdBoxes[jdx - 1][1]) == 1):
                createdBoxes[jdx], createdBoxes[jdx - 1] = createdBoxes[jdx - 1], createdBoxes[jdx]
            jdx = jdx - 1
        idx = idx + 1
    return createdBoxes

def main():
    boxList = []
    inFile = open('boxes.txt','r')
    for line in inFile:
        line = line.rstrip('\n')
        tempBox = line.split(' ')
        if len(tempBox) == 1:               ## If the length of the tempBox list is 1, this will be the number of boxes in the file.
            numBoxes = int(tempBox[0])
        if len(tempBox) != 1:               ## If the length of the tempBox list is not 1, it will contain the dimensions of a box.
            tempBox = tempBox[0:3]
            tempBox[0] = int(tempBox[0])
            tempBox[1] = int(tempBox[1])
            tempBox[2] = int(tempBox[2])
            boxList.append(tempBox)

    createdBoxes = []                       ## Boxes are identified by giving them a unique name along with a sorted list of their 
    for i in range(1, numBoxes + 1):        ## dimensions.
        boxName = 'box' + str(i)
        boxTuple = (boxName,Box(boxList[i-1][0],boxList[i-1][1],boxList[i-1][2]))
        createdBoxes.append(boxTuple)

    sortedBoxes = bubbleSort1(createdBoxes) ## Now that all the boxes have been created, they are sorted according to their smallest 
                                            ## dimension.
    linkQ = Queue()                         ## The sorted boxes are put into a queue which will be used to check nesting of the boxes.
    linkQ.enqueue(sortedBoxes)

    lngLen = 0                              ## lngLen will be used to store the value of the length of the longest nested list.
    longList = []
    listOfLists = []
                                              ## a list of boxes sorted by smallest dimension.
    while (linkQ.isEmpty() == False):
        check = linkQ.dequeue()             ## Each iteration of the while loop takes the first list off the queue. This will be a list of
        chLen = len(check)                  ## boxes sorted by smallest dimension. Since we will be checking pairs of boxes, to see if one nests
        lastBox = check[0]                  ## inside another, the box with the largest, 'small' dimension is initialized as being the last box to be checked. 
        tempLinks = [lastBox]               ## The tempLinks list will hold the list of boxes that nest inside the previous one, starting
        for box in check[1:]:               ## with the box that has the largest 'small' dimension. 
            if box[1].doesFit(lastBox[1]) == True:
                tempLinks.append(box)
                lastBox = box
            elif box[1].doesFit(lastBox[1]) == False:   ## If a box does not fit inside the previous one, the number of boxes left to be 
                idx = check.index(box)                  ## checked in the list is compared with the number of boxes in the list that 
                chLen = len(check) - idx                ## most recently been added to the queue. If it is possible that a longer nested list
                if linkQ.isEmpty() == False:            ## could be created by considering nests starting with this box, the list boxes that have
                    qLen = len(linkQ.queue[-1])         ## not been checked up to this point are added to a queue with this box at the top.
                else:
                    qLen = 0 
                if (qLen < chLen):
                    linkQ.enqueue(check[idx:])
          
        if len(tempLinks) > lngLen:                     ## The length of the temporary list of nested boxes is checked against the 
            lngLen = len(tempLinks)                     ## length of the longest list found yet. If it is greater, the other is erased
            longList = []                               ## and the list is now stored as the longest list. If both lists contain the same
            for item in tempLinks:                      ## number of boxes, a list containing both lists is created.
                longList.append(item)
            listOfLists = []
        elif len(tempLinks) == lngLen:
            listOfLists.append(longList)
            listOfLists.append(tempLinks)            
        if (linkQ.isEmpty() == True) and (len(check[1:]) >= lngLen):    ## If the queue is empty, and it is still possible that a longer
            linkQ.enqueue(check[1:])                                    ## chain exists, the list of remaining boxes is added to the queue. 

    if lngLen > 1:
        print 'Largest Subset of Nesting Boxes'
        if len(listOfLists) > 1:
            for nestList in listOfLists:
                for box in nestList:
                    print box[1].dimension
                print
        else:
            for box in longList:
                print box[1].dimension
    else:
        print 'No Nesting Boxes'
    inFile.close()
main()
    
