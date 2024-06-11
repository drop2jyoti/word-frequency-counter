import matplotlib.pyplot as plt
import string
import numpy as np
import sys

def count_frequency(text):
    # Create an empty dictionary
    d = dict()
    print(text)
    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Remove the punctuation marks from the line 
        line = line.translate(line.maketrans("", "", string.punctuation)) 
         # Remove the digits marks from the line 
        line = line.translate(line.maketrans("", "", string.digits)) 
        print("Line -> " + line)
        # Split the line into words
        words = line.split(" ")
        # Iterate over each word in line
        for word in words:
            if word == "":
                continue
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

    # sort the dictionary by the frequency count values, in Descending order
    sortedDict = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
    print(sortedDict)
    return sortedDict
   
def write_to_file(sortedDict, file_location):  
    # make a new text file, then write results to that
    with open(file_location, 'w') as f:
        for key in list(sortedDict.keys()):
            f.write(f"{key} ----> {sortedDict[key]}\n")  

def print_the_words_with_frequency(sortedDict):
    for key in list(sortedDict.keys()):
        print(f"{key} ===> {sortedDict[key]}\n")  

def plot_graph(sortedDict):
    data_words = sortedDict.keys()
    words_counts = sortedDict.values()
    indexes = np.arange(len(data_words))
    width = 0.7
    plt.bar(indexes, words_counts, width)
    plt.xticks(indexes + width * 0.5, data_words)
    plt.show()




def main():
    user_input = input("Read text from console or local file location. Choose 1 for console and 2 for file :")
    result = None
    if user_input == "1":
        print("Enter Text. To continue entering more press enter or else q to quit: ")
        #result = count_frequency(text_input)
        lines = []
        for line in sys.stdin:
            if 'q' == line.rstrip():
                break
            lines.append(line)
        text_input = '\n'.join(lines)
        print(text_input)
        result = count_frequency(text_input)
    elif user_input == "2":
        file_name = input("Enter relative path of file : ")
        text_input = open(file_name, "r")
        result = count_frequency(text_input)
    else:
        print("Incorrect choice!")

    if result != None:
        print("\n\n######## Word Frequency Occurrence Details ########")
        print("Total number of words:" , len(result))
        print("Most common word used is: " , max(result, key=result.get))
        print("######################################################")
        print("{}   ===>   {}".format("WORDS", "COUNT"))
        print("\n")
        print_the_words_with_frequency(result)
        print("#####################################################")
        plot_graph(result)
    else:
        print("Result is unavailable")
       
if __name__ == "__main__":
    main()