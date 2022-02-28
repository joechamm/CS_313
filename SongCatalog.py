##  File: SongCatalog.py
##
##  Description: Creates an editable catalog of artists and songs.
##
##  Student's Name: Joseph Cunningham
##
##  Student's UT EID: jsc2539
##
##  Course Name: CS 313E 
##  
##  Unique Number: 53330 
##
##  Date Created: 3 Mar 2011
##
##  Date Last Modified: 4 Mar 2011


## Create the songcatalog class with the initial attribute catalog which is a ditionary.

class SongCatalog (object):

  def __init__ (self):
    self.catalog = {}


## The addSong acts by checking first if the artist exists in the catalogs list of keys. If not it is added as a key with value 'title' and if
## it is a key in the dictionary the song is added as an entry to the list of values of the artist. 


  def addSong (self, artist, title):
    if self.catalog.has_key(artist) == True:
        self.catalog[artist] = self.catalog[artist].append(title)
    else:
        self.catalog[artist] = [title]
        
## The deleteSong function checks first if a value has been entered for the artist and title. If neither value is entered the user is informed that
## they have not entered proper values. The case where the artist is left blank first asks the user if they wish to delete all songs by that title.
## If an artist is entered, but no song is indicated, all values for the artist are deleted and the artist is removed from the dictionary's list of keys.
## Finally if both song and artist are entered, and the catalog contains both, the song is removed from the catalog.
        
  def deleteSong (self, artist, title):
    if ((artist.isspace() == True) or len(artist)== 0) and ((title.isspace() == True) or (len(title) == 0)):
        print 'You have not entered valid input. Please try again'
    elif ((artist.isspace() == True) or (len(artist) == 0)):
        yesNo = raw_input('You have not entered an artist. Do you want all songs of that title to be deleted? y/n ')
        if yesNo.upper() == 'Y':
            for key in self.catalog:
                for j in self.catalog[key]:
                    if j == title:
                        del self.catalog[key]
    if ((title.isspace() == True) or (len(title) == 0)):
        if self.catalog.has_key(artist) == True:
            yesNo = raw_input('Do you want to wish to remove this artist from the catalog? y/n ')
            if yesNo.upper() == 'Y':
                self.catalog.pop(artist)
        else:
            print 'That artist is not located in this list.'
    if ((title.isspace() == False) and (len(title) != 0)) and ((artist.isspace() == False) and (len(artist) != 0)):             
        for i in self.catalog[artist]:
            if i == title:
                del self.catalog[key]


## The searchCatalog determines in the same way as the deleteSong function whether or not an artist and/or values are entered, then
## returns the values that the user has identified if they exist in the catalog, and lets the user know if they are not in the catalog.

  def searchCatalog (self, artist, title):
    if ((artist.isspace() == True) or (len(artist) == 0)):
        if ((title.isspace() == True) or (len(title) == 0)):
            print 'Please enter a valid artist and/or song.'
        else:
            hasTitle = 0
            for key in self.catalog:
                for value in self.catalog[key]:
                    if title in value:
                        print 'Artist: ', key
                        print 'Song: ', title
                        hasTitle = 1
            if hasTitle == 0:
                print 'This song is not in the catalog.'
    else:
        if self.catalog.has_key(artist) == True:
            if (title.isspace() == True) or (len(title) == 0):
                print 'Songs by', artist
                for value in self.catalog[artist]:
                    print value
            elif title in self.catalog[artist]:
                print 'Artist: ', artist
                print 'Song: ', title
        else:
            print 'Artist not found in catalog.'


            
            for value in self.catalog[artist]:
                if value == title:
                    print 'Artist: ', artist
                    print 'Song: ', self.catalog[artist]
        

## The display Catalog lists all songs and artists in the catalog


  def displayCatalog (self):
    tempList = []
    for key in self.catalog:
        tempList.append(key)
    tempList.sort()
    for item in tempList:
        print 'Artist: ', item
        for val in self.catalog[item]:
            print 'Song: ', val
    print

## The readfile takes in the file specified as the starting input.


  def readFile (self, fileName):
    infile = open (fileName, 'r')
    onOff = 0
    for line in infile:
        line = line.rstrip('\n')
        if onOff == 0:
          oldList = line.split(': ')
          onOff = 1
          self.catalog[oldList[1]] = []          
        if (line.find(': ')) != -1:
            tempList = line.split(': ')
            if tempList[0] == 'Artist':
                if self.catalog.has_key(tempList[1]) == False:
                    self.catalog[tempList[1]] = []
            if tempList[0] == 'Title':
                titArtist = str(oldList[1])
                
                if self.catalog.has_key(str(oldList[1])) == True:
                    self.catalog[str(oldList[1])].append(str(tempList[1]))
                else:
                    self.catalog[str(oldList[1])] = str(tempList[1])
            oldList = tempList
    infile.close()
    
  def saveFile (self):
    outfile = open('songs.txt','w')
    tempList = []
    for key in self.catalog:
        tempList.append(key)
    tempList.sort()
    for item in tempList:
        for val in self.catalog[item]:
            outfile.write('Artist ' + item + '\n')
            outfile.write('Song: ' + val + '\n')
            outfile.write('\n')
    outfile.close()
    

    
def main():
  songCat = SongCatalog()
  switch = 0

  while switch == 0:
    print 'Song Catalog Menu'

    print '1. Import songs from a file'

    print '2. Add a song'

    print '3. Delete a song'

    print '4. Search for a song'

    print '5. Display all songs'

    print '6. Exit program'
    selection = input('Enter selection (1 - 6): ')
    if selection > 6 or selection < 1 or (selection != int(selection)) :
      selection = input('Please enter a valid entry: ')
    if selection == 1:
      fileName = raw_input('Please enter the absolute path name of the file to import songs from: ')
      songCat.readFile(fileName)
    if selection == 2:
      print 'Add a Song'
      print
      artist = raw_input('Enter Artist: ')
      title = raw_input('Enter title: ')
      songCat.addSong(artist,title)
    if selection == 3:
      print 'Delete a song'
      print
      artist = raw_input('Enter Artist: ')
      title = raw_input('Enter title: ')
      songCat.deleteSong(artist, title)
    if selection == 4:
      print 'Search for an Artist / Song'
      print
      artist = raw_input('Enter Artist: ')
      title = raw_input('Enter title: ')
      songCat.searchCatalog(artist, title)
    if selection == 5:
      songCat.displayCatalog()
    if selection == 6:
      print 'Thank you, for using the Song Catalog.'
      switch = 1
      songCat.saveFile()
      
main()




