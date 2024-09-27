import time
import matplotlib.pyplot as plt #import rec'd things
import random
from DictionaryBST import *


def measure_search_time(dictionary_bst, search_words):
    start_time = time.time()    #start timer before the search starts
    for word in search_words:
        word = dictionary_bst.search(word.getWord()) #search the text for the word
    end_time = time.time()
    return end_time - start_time #return words searched (and time) to see wordssearched/s

def measure_time_for_different_sizes(dictionary_bst, M, all_words):
    search_words = random.sample(all_words, M)
    elapsed_time = measure_search_time(dictionary_bst, search_words) #search the bst with different sizes
    return elapsed_time

sizes = [99171, 139719, 86017]  # length of french/eng/esp
names = ['English', 'French', 'Spanish']
times = []

for size, name in zip(sizes, names): #easy eay to get each individual name and size by creating a tuple
    bst = DictionaryBST()
    if name == 'English':
        bst.load('english')     #load dictionary w/ proper file
    elif name == 'French':
        bst.load('french')
    elif name == 'Spanish':
        bst.load('spanish')
    
    all_words = bst.extractInOrder()    #extract the words in order
    
    # Measure time
    elapsed_time = measure_time_for_different_sizes(bst, 50000, all_words) #get the time
    times.append(elapsed_time)
    print(f"Searched the {name} dict with total size {size}, in {elapsed_time} seconds.")

plt.figure(figsize=(10, 6)) #figsize helps with the grid
plt.scatter(sizes, times, color=['blue', 'green', 'red']) #do a scatter plot as a normal plot will look weird due to
plt.xlabel('Dictionary Size (N)')                         #odd spanish results (most of the time)
plt.ylabel('Time (sec)')       #print the plot with proper titles
plt.title('Time vs. Dictionary Size (N) with M fixed at 50,000')
plt.grid(True)
plt.show()