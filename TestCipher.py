##  File: TestCipher.py
##
##  Description: Tests the accuracy of the substitution and vigenere ciphers.
##
##  Student's Name: Joseph Cunningham
##
##  Student's UT EID: jsc2539
##
##  Course Name: CS 313E 
##
##  Unique Number: 53330
##
##  Date Created: 11 Feb 2011
##
##  Date Last Modified: 11 Feb 2011


import string

##  Create the substitution cipher by transforming the message to be encoded into
##  their numerical values, then obtaining the order in which each letter appears in
##  the alphabet.  These points are then evaluated at their index in the permuted list
##  list of letters, which is the cipherTex. 

def substitution_encode ( strng ):
    print 'Substitution Cipher'
    print 
    inTex = strng.split(' ') 
    cipherTex = ['q','a','z','w','s','x','e','d','c','r','f','v','t','g','b','y','h','n','u','j','m','i','k','o','l','p']
    tex = []
    encodedWord = []
    for word in inTex:
        tempWord = ''
        for ch in word:
            idx = ord(ch) - ord('a')
            tempWord = tempWord + cipherTex[idx]
        encodedWord.append(tempWord)
    print 'Encoded Text: ',
    for word in encodedWord:
        print word,
    print

##  The decode function reverses the encode process, by locating the integer value
##  associated to each letter in the encoded message and assigning the appropriate letter
##  according to the usual alphabetical index (i.e. a,b,c...,y,z.). The original word is then
##  reconstructed by adjoining these letters together.


def substitution_decode ( strng ):
    cipherTex = ['q','a','z','w','s','x','e','d','c','r','f','v','t','g','b','y','h','n','u','j','m','i','k','o','l','p']
    inTex = strng.split(' ') 
    tex = []
    decodedWord = []
    
    for word in inTex:
        tempWord = ''
        for ch in word:
            idx = cipherTex.index(ch) + ord('a')
            tempLet = chr(idx)
            tempWord = tempWord + tempLet
        decodedWord.append(tempWord)
    print 'Decoded Plain Text: ',
    for word in decodedWord:
        print word,
    print

##  The vigenere_encode function takes in two values, the message to be encoded and the passphrase with which to encode the message.
##  The encoding works via a one-to-one pairing of each letter in the message and its index, and the index of the passphrase modulo
##  the length of the passphrase. This one-to-one pairing is accomplished by adding the alphabetical index of the letter to be encoded
##  and the alphabetical index of the appropriate letter in the passphrase, and 'wrapping around' modulo 26. 

def vigenere_encode ( strng, passwd ):
    print 'Vigenere Cipher'
    print
    vStrng = strng
    passWord = passwd
    passPh = []
    inTex = vStrng.split(' ') 
    for ch in passWord:
        passPh.append(ch)
    vEncTxt = []
    passLen = len(passWord)
    enCodWord = []
    count = 0
    for word in inTex:
        tempWord = ''
        for ch in word:
            idx = ((ord(ch)-ord('a'))+ord((passPh[count])) - ord('a'))%26
            tempLet = chr((idx+ord('a')))
            tempWord = tempWord + tempLet
            count = (count + 1)%passLen
        enCodWord.append(tempWord)
    print 'Encoded Text: ',
    for word in enCodWord:
        print word,
    print


##  The vigenere encoding process is reversed by first finding the difference of the two indexes modulo 26
##  then returning the value of the original letter's index. Using this value, the original letter is produced
##  by simply adding the Python integer value of 'a' to return the letter.
    
def vigenere_decode ( strng, passwd ):
    dStrng = strng
    passWord = passwd
    passPh = []
    inTex = dStrng.split(' ') 
    for ch in passWord:
        passPh.append(ch)
    dDecTxt = []
    passLen = len(passWord)
    dCodWord = []
    count = 0
    for word in inTex:
        tempWord = ''
        for ch in word:
            passLet = passPh[count]
            idx = ((ord(ch)-ord('a'))-((ord(passLet)-ord('a'))))%26 + ord('a')
            tempLet = chr(idx)
            tempWord = tempWord + tempLet
            count = (count + 1)%passLen
        dCodWord.append(tempWord)
    print 'Decoded Plain Text: ',
    for word in dCodWord:
        print word,
    print

def main():
    print 'Substitution Cipher'
    print
    strngEncode = raw_input('Enter Plain Text to be Encoded: ')
    substitution_encode ( strngEncode )
    strngDecode = raw_input('Enter Encoded Text to be Decoded: ')
    substitution_decode ( strngDecode )
    vStrngEncode = raw_input('Enter Plain Text to be Encoded: ')
    passPhrase = raw_input('Enter Pass Phrase (no spaces allowed): ')
    while passPhrase.isalpha() == False:
        passPhrase = raw_input('Please enter a Pass Phrase with no spaces: ')
    vigenere_encode(vStrngEncode,passPhrase)
    dStrngDecode = raw_input('Enter Encoded Text to be Decoded: ')
    dPhrase = raw_input('Enter Pass Phrase: ')
    while dPhrase.isalpha() == False:
        passPhrase = raw_input('Please enter a Pass Phrase with no spaces: ')
    vigenere_decode(dStrngDecode,dPhrase)


main()

