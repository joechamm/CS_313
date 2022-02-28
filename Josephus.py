#  File: Josephus.py

#  Description: Determines the order in which a group of soldiers is to be executed.

#  Student Name: Joseph Cunningham

#  Student UT EID: jsc2539

#  Course Name: CS 313E

#  Unique Number: 53330 

#  Date Created: 22 March 2011

#  Date Last Modified: 25 March 2011


class Link(object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class CircularList(object):
    def __init__ ( self ):
        self.head = Link(None, None)
        self.head.next = self.head

    def insert ( self, item ):
        if self.head.next == self.head:         ## First check and see if there is anything in the list
            self.head.next = Link(item)         ## If not, create a link that points to itself.
            self.head.next.next = self.head.next## If the list is not empty, the head of the list will not point to itself.
        else:                                   ## The item is inserted at the end of the list, which 
            probe = self.head.next              ## is located by finding by finding the link pointing to the first link created.
            while probe.next != self.head.next: ## We now point this link to the item being inserted, and point the item to the 
                probe = probe.next              ## first link.
            probe.next = Link(item, probe.next)  
        
    def find ( self, key ):                     
        if self.head.next != self.head:
            probe = self.head.next
            while (probe.next != self.head.next):
                if probe.data == key:
                    return probe
                else:
                    probe = probe.next
            if probe.next == self.head.next:
                return False
        else:
            return False
            
    def delete ( self, key ):                   ## First check to see if the item to be deleted is the one that the dummy header
        if key == self.head.next:               ## points to. If so, the dummy header must be pointed to the next viable link, so 
            self.head.next = key.next           ## traversal is still possible.
        st = str(key.data)
        st += ' was executed.'
        key.next = None
        key.data = None
        print st

    def deleteAfter ( self, start, n ):         ## The sad fellow is the one who is currently facing the axe.
        if self.find(start) != False:           ## The deleteAfter function is initialized with the starting conditions given      Since happy fellow now points to the next
            sadFellow = self.find(start)        ## in the text file. If the starting soldier cannot be found in the list, this indicates that the format of the input file is somehow
            finished = False                    ## incorrect, and avoids entering an endless while loop. If the starting soldier is not the first to be executed, he has been skipped over
            pointer = sadFellow                 ## and is now a happy fellow. The executions can now start, and happen on every nth iteration of the next while loop. If the one to be executed
            while not finished:                 ## next is still a happy fellow, it means that there is only one man left in the list, and he's the one to get away.
                if pointer.next == sadFellow:
                    finished = True
                else:
                    pointer = pointer.next
            happyFellow = pointer
            counter = 1
            while sadFellow != happyFellow:
                if (counter == n):
                    happyFellow.next = sadFellow.next
                    self.delete(sadFellow)
                    sadFellow = happyFellow.next
                    counter = 1
                else:
                    happyFellow = sadFellow
                    sadFellow = happyFellow.next
                    counter += 1
            st = str(happyFellow.data)
            st += ' gets away!'
        else:
            st = 'Input has not been given in correct format. Please ensure that line \n 1) number of soldiers \n 2) soldier to start counting from \n 3) the elimination number'
        print st 

### Return a string representation of a Circular List
    def __str__ ( self ):
        if self.head.next == self.head:  
            st = ' is empty.'
            return str(self) + st
        else:
            st = ''
            probe = self.head.next  
            while probe.next != self.head.next: 
                st += str(probe.data)
                st += '\n'
                probe = probe.next  
            st += str(probe.data)
            return st


def main():
    lineNum = 1
    infile = open('josehus.txt','r')
    for line in infile:
        line = line.rstrip('\n')
        if lineNum == 1:
            numSoldiers = int(line)
        elif lineNum == 2:
            index = int(line)
        elif lineNum == 3:
            n = int(line)
        lineNum += 1
    
    solList = range(1,numSoldiers + 1)
    cirList = CircularList()
    for sol in solList:
        cirList.insert(sol)
    cirList.deleteAfter(index, n)

main()
