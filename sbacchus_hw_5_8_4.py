"""
Shane Bacchus
Class: CS 521 - Fall 1
Date:10/10
Homework Problem # 4
Description of Problem (just a 1-2 line summary!):
Create function to turn file into list with words that occur once
"""
import string # Used to remove punctuation

def list_to_once_words(file_name):
    """Convert file to list of words that occurred once"""
    print (list_to_once_words.__doc__)
    
    try:
        temp_file = open(file_name,"r") #  open the file for reading
    except FileNotFoundError:
        print('File does not exist. Program is terminating') #  if file not found terminate program
        exit()

    x_list = [] #  create a list to store words from file
    
    for line_str in temp_file:
        for word in line_str.split():
            x_list.append(word.lower()) #  append words to list
   
    
    #  Remove Punctuation
    removed_punctuation = [''.join(c for c in s if c not in string.punctuation) for s in x_list]
    
    #  New list where words occurred once
    final_list = [x for x in removed_punctuation if removed_punctuation.count(x) == 1] 
    return final_list
    

if __name__ == "__main__":
    file_name = input("Please enter a file name of text words including the extension: ")
    print(list_to_once_words(file_name))