import time
import random
import matplotlib.pyplot as plt #import rec'd things
from DictionaryBST import *

def generate_random_words(words_list, num_words):
    return random.sample(words_list, min(num_words, len(words_list)))

bst = DictionaryBST()
    
bst.load("english") #load dictionary english with DictionaryBST

all_words = bst.extractInOrder() #get the words in order
all_words_list = [word.getWord() for word in all_words] #set it to the actual words

Mvals = list(range(10000, 99172, 10000)) #create a list with 10000,20000,30000... loaded
times = []

for M in Mvals:
    random_words = generate_random_words(all_words_list, M) #make the random word list
    start_time = time.time()
    for word in random_words:#start timer and search using built-in search
        bst.search(word)
    end_time = time.time()
    
    elapsed_time = end_time - start_time #print the time and M
    times.append(elapsed_time)
    print(f"Completed searching {M} words in {elapsed_time} seconds.")

plt.figure(figsize=(10, 6)) #figsize helps with the gridlines/scaling
plt.plot(Mvals, times, marker='o')
plt.xlabel('Number of Random Words (M)')
plt.ylabel('Time (seconds)')
plt.title('Time vs Number of Random Words')
plt.grid(True)              #plot the results, set the labels and stuff
plt.show()
