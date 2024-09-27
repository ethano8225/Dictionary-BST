##Made by: Ethan O'Connor
##SPIRE ID: 34445111

from Word import *
class Node:
    def __init__(self, data, index):    #more or less the same thing as in class
        self.data = data                #+index
        self.index = index
        self.left = None                # child nodes
        self.right = None
    def __str__(self):
        return str(self.data)

class DictionaryBST:
    def __init__(self):
        self.root = None
        self.__nodes = 0      #set required instance 
        self.__levels = 0     #variables to default values

    def load(self, file_name):
        """Load the userinputted file name's words into a tree"""
        loadname= open(file_name+".txt", 'r') 
        for line in loadname:
            word = Word(line.strip(), file_name)   #load the file, read the lines(w/ for loop)
            self.insert(word)                      #insert the words as a "Word" class

    def insert(self, word):
        """Set the initial root node or use recursion to set a node in the correct spot"""
        if not self.root:                           #check if the root node is not none
            self.root = Node(word,0)     #if it is, set the root node, levels, etc
            self.__nodes += 1
        else:
            self._recInsert(self.root, word, 0) #if not, recursively find the correct spot to insert it

    def _recInsert(self, node, word, level):
        """Insert the node at the correct point in the tree using recursion"""
        nodeword=node.data.getWord()
        if word.getWord() < nodeword:       #for both inserting to the right and left, check if there is a
            if node.left:                   #node present,update level and node
                self._recInsert(node.left, word, level+1)
            else:
                node.left = Node(word, 2*node.index+1)  #if not, set the Word at the given index value,
                self.__nodes += 1                       #update the tree info and levels if needed
                self.__levels = max(self.__levels, level+1)
        else:
            if node.right:
                self._recInsert(node.right, word, level+1)
            else:
                node.right = Node(word, 2*node.index+2)   #same idea here
                self.__nodes += 1
                self.__levels = max(self.__levels, level+1) 

    def getSize(self):
        """return node count (self.__nodes)"""
        return self.__nodes 

    def getMaxLevel(self):
        """return max level (self.__levels)"""
        return self.__levels

    def extractInOrder(self):
        """Use recursive function to get the words list"""
        words_list = []
        self._recinOrder(self.root, words_list) #call the recursive function to calculate words_list
        return words_list                       #return words_list once recursion is done

    def _recinOrder(self, node, words_list):
        """Recursive func. to set words_list for extractInOrder"""
        if node:                                     #check if node is not none, if there is a node
            self._recinOrder(node.left, words_list)  #go to left side first
            words_list.append(node.data)
            self._recinOrder(node.right, words_list)

    def show(self, option='word'):
        """Show the tree in different ways"""
        if option == 'word':
            print("\nThe BSTree using type -word- looks like:") #print the correct text and then provide the output
        elif option=='id':
            print("The BSTree using type -id- looks like:")
        elif option=='index':
            print("The BSTree using type -index- looks like:")
        self._recShow(self.root, 0, option)
        print()

    def _recShow(self, node, level, option):
        """recursively show tree data for show"""
        if node:
            self._recShow(node.right, level+1, option)
            if option == 'word':
                print('    '*level+f"{node.data.getWord()}")    #use the same idea as above to print the correct data
            elif option == 'id':
                print('    '*level+f"{node.data.getID()}")
            elif option == 'index':
                print('    '*level+f"{node.index}")
            self._recShow(node.left, level+1, option)

    def search(self, word):
        """Search if a word is present is in the tree"""
        current = self.root
        while current:
            if word == current.data.getWord():
                return current.data             # return the word found as a class
            elif word < current.data.getWord():
                current = current.left          # Move to the left child/right child
            else:
                current = current.right  
        return None                             # return none if it isnt found

    def spell_check(self,filename):
        """Spell check the given file"""
        print()
        punc=['"',"©","!","´","'",".",",","‚","(",")","-","[","]","{","}",";",":","’","@","\\","<",">","#","/","?","$","%","^","&","*","_","~"] #only ones needed for the provided letter, 
                                        
        # ()-[]{};:’@\\<>#//?$%^&*_~
        #all of these are from the provided list don't change anything, i think there is 
        #something weird going on with the encoding type or sth. my vscode output for the initial print(lines) does not
        #match the pdf's or how my notepad sees the letter.txt file (Â is added in a lot of places in the vscode output)
        
        #on top of this, the letter.txt file on notepad doesnt match the pdf either so i tried to copy it from both the 1st place it is
        #provided in the pdf, and in the actual code (they are slightly different). my vscodes output still doesn't
        #match the letter.txt in notepad or the pdf after doing these switches, so i'm just confused, 
        #it says vscode is in utf-8, and the text file says that as well (and open() uses utf-8 by default in python3)
        
        #i added these 3 different text files in my ZIP for this exact reason, pdf1 represents the first time the txt file is shown,
        #pdf2 represents the time it is shown in the code output

        #If you'd like to see the vscode outputs yourself, you can email me at eroconnor@umass.edu
        #and I will be happy to provide whatever output you request

        file_name=open(filename,"r",encoding='utf-8')
        for line in file_name:      
            print(line,end="")     
            line=line.lower().strip().replace("  "," ").split(" ")
            i=0         #lowercase the line, strip, replace double space with space, and split it
            check="["   #into a list
            for word in line:       #build the word-checker piece by piece with str concatenation (can use a list as well)
                for char in punc:
                    word=word.replace(char, "") #replace weird characters for each word
                wordclass=self.search(word)     #search for the word, if present,
                if wordclass is not None:       #add the ID for it
                    check+="-"+wordclass.getID()
                else:
                    check+="-no ID"         #despite the weird vscode output it still works pretty well8
            check+="-]"                     #to check most words
            print(check)