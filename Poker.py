##  File: Poker.py
##
##  Description: Simulates a hand of poker, and returns the rank of the winning hand.
##
##  Student's Name: Joseph Cunningham
##
##  Student's UT EID: jsc2539
##
##  Course Name: CS 313E 
##
##  Unique Number: 53410
##
##  Date Created: 25 Feb 2011
##
##  Date Last Modified: 25 Feb 2011


import string, math, random

class Card(object):

##  A card object with a suit and rank.

    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('S', 'D', 'H', 'C')


##  Creates a card with the given rank and suit.
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
##  Returns the string representation of a card.

    def __str__(self):
        if self.rank == 11:
            rank = 'J'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 14:
            rank = 'A'
        else:
            rank = self.rank
        return str(rank) + self.suit

    def __cmp__ (self, other):
        if (self.rank < other.rank):
            return -1
        elif (self.rank > other.rank):
            return 1
        else:
            return 0

##  A deck containing 52 cards.

class Deck(object):

##  Creates a full deck of cards.

    def __init__(self):
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card (rank, suit)
                self.deck.append (c)

##  Shuffles the cards.
    def shuffle(self):

        for i in range(7):
            random.shuffle(self.deck)
        

##  Removes and returns the top card or None 
##        if the deck is empty.

    def deal(self):

        if len(self) == 0:
           return None
        else:
           return self.deck.pop(0)

##  Returns the number of cards left in the deck.

    def __len__(self):
        return len(self.deck)

##  Returns the string representation of a deck.

    def __str__(self): 
        result = ''
        for c in self.deck:
            result = result + str(c) + '\n'
        return result

class Poker (object):
    def __init__ (self, numHands):
        self.deck = Deck()
        self.deck.shuffle()
        self.hands = []
        numCards_in_Hand = 5

        for i in range (numHands):
            hand = []
            for j in range (numCards_in_Hand):
                hand.append (self.deck.deal())
            self.hands.append (hand)


    def play(self):
        handDict = {}
        def isRoyal (self, hand):
            self.hand = hand            
            isTrue = 1
            i = 0
            while (isTrue == 1) and (i < 5):
               if self.hand[i].rank == ((4-i) + 10):
                    if self.hand[i].suit == self.hand[0].suit:
                        isTrue = 1
                        i = i + 1
                    else:
                        isTrue = 0
               else:
                   isTrue = 0
            if isTrue == 1:
                return [10, 'Royal Flush']
            else:
                return [0, 'No Winner']

        def isStraightFlush (self, hand):
            self.hand = hand
            isTrue = 1
            i = 1
            suits = []
            for j in range(5):
                suits.append(self.hand[j].suit)
            while (isTrue == 1) and (i < 5):
                if (self.hand[i].rank == (self.hand[i - 1].rank - 1)):
                    isTrue = 1
                    i = i + 1
                elif (self.hand[i-1].rank==14) and (self.hand[i].rank == 5) and (i == 1):
                    isTrue = 1
                    i = i + 1
                else:
                    isTrue = 0
            
            if (isTrue == 1) and (suits.count(suits[0]) == 5):
                return [9, 'Straight Flush']
            elif isTrue == 0:
                return [0, 'No Winner']

        def isFour (self, hand):
            self.hand = hand
            if self.hand[0].rank == self.hand[1].rank == self.hand[2].rank == self.hand[3].rank:
                isTrue = 1
            elif self.hand[1].rank == self.hand[2].rank == self.hand[3].rank == self.hand[4].rank:
                isTrue = 1 
            else:
                isTrue = 0
            if isTrue == 1:
                return [8, 'Four of a Kind']
            else:
                return [0, 'No Winner']

        def isFull (self, hand):
            self.hand = hand
            ranks = []
            for q in range(5):
                ranks.append(self.hand[q].rank)
            for i in range(len(self.hand)):
                if ranks.count(self.hand[i].rank) == 3:
                    for j in range(len(self.hand)):
                        if ranks.count(self.hand[j].rank) == 2:
                            return [7, 'Full House']

            return [0, 'No Winner']    

        def isFlush (self, hand):
            self.hand = hand
            suits = []
            for i in range(5):
                suits.append(self.hand[i].suit)
            if suits.count(suits[0]) == 5:
                return [6, 'Flush']
            else:
                return [0, 'No Winner']

        def isStraight (self, hand):
            self.hand = hand
            isTrue = 1
            i = 1
            while (isTrue == 1) and (i < 5):
                if self.hand[i].rank == (self.hand[i - 1].rank - 1):
                    isTrue = 1
                    i = i + 1
                elif (self.hand[0].rank == 14) and (self.hand[1].rank) == 5:
                    isTrue = 1
                    i = i + 1
                else:
                    isTrue = 0

            if isTrue == 1:
                return [5, 'Straight']
            else:
                return [0, 'No Winner']


        def isThree (self, hand):
            self.hand = hand
            ranks = []
            for i in range(5):
                ranks.append(self.hand[i].rank)
            for i in range(5):
                if ranks.count(self.hand[i].rank) == 3:
                    return [4, 'Three of a Kind']
            return [0, 'No Winner']


        def isTwo (self, hand):
            self.hand = hand
            ranks = []
            for i in range(5):
                ranks.append(self.hand[i].rank)
            for i in range(5):
                if (ranks.count(self.hand[i].rank) == 2):
                    val = self.hand[i].rank
                    for j in range(5):
                        if (self.hand[j].rank != self.hand[i].rank) and (ranks.count(self.hand[j].rank) == 2):
                            return [3, 'Two Pair']
            return [0, 'No Winner']


        def isOne (self, hand):
            self.hand = hand
            ranks = []
            for i in range(5):
                ranks.append(self.hand[i].rank)
            for i in range(5):
                if ranks.count(self.hand[i].rank) == 2:
                    return [2, 'One Pair']
            return [0, 'No Winner']

        def isHigh (self, hand):
            self.hand = hand
            return [1, 'High Card']

        for i in range (len(self.hands)):
            sortedHand = sorted(self.hands[i], reverse = True)
            hand = ''
            for card in sortedHand:
                hand = hand + str(card) + ''
            h = [0,0]
            h = isRoyal(self,sortedHand)
            if h[0] == 0:
                h = isStraightFlush(self,sortedHand)
            if h[0] == 0:
                h = isFour(self, sortedHand)
            if h[0] == 0:
                h = isFull(self, sortedHand)
            if h[0] == 0:
                h = isFlush(self, sortedHand)
            if h[0] == 0:
                h = isStraight(self, sortedHand)
            if h[0] == 0:
                h = isThree(self, sortedHand)
            if h[0] == 0:
                h = isTwo(self, sortedHand)
            if h[0] == 0:
                h = isOne(self, sortedHand)
            if h[0] == 0:
                h = isHigh(self, sortedHand)
            formatHand = str(self.hand[0])+' '+str(self.hand[1])+' '+str(self.hand[2])+' '+str(self.hand[3])+' '+str(self.hand[4])

            totalPoints = h[0]*(15**5) + self.hand[0].rank*(15**4) + self.hand[1].rank*(15**3) + self.hand[2].rank*(13**2) + self.hand[3].rank*13 + self.hand[4].rank
            handDict[formatHand] = [h[1],totalPoints]
            
        handCounter = 1
        for key in handDict:
            print 'Hand %d: ' % (handCounter), key
            handCounter = handCounter + 1
        print
        handCounter = 1
        mostPoints = 0
        for key in handDict:
            print 'Hand %d: ' % (handCounter), handDict[key][0]
            if handDict[key][1] > mostPoints:
                winner = 'Hand %d' % (handCounter)
                mostPoints = handDict[key][1]
            handCounter = handCounter + 1
        print 
        print winner, 'wins.' 
                
        
def main():
    numHands = input('Enter the number of hands to play(from 2 to 6): ')
    while (6 < numHands) or (numHands < 2):
        numHands = input('Please enter a number between 2 and 6 for the number of hands: ')
    game = Poker(numHands)
    game.play()
main()
