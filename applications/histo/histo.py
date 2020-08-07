# Your code here
import sys


if len(sys.argv) < 2 or sys.argv[1] != 'robin.txt':
    print('Correct Usage: histo.py <filename>.txt')
    # return
else:
    filename = sys.argv[1]

    # open file and get text
    with open(filename) as f:
        text = f.read()
        
    # remove ignored characters and get everything in lower case
    ignoredChars = ["\"", ":", ";", ",", ".", "-", "+" ,"=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]

    cleanText = ""
    for char in text:
        if char not in ignoredChars:
            cleanText = cleanText + char.lower()

    # split text into words and get word count for each and length of longest word
    words = cleanText.split()

    wordCounts = {}
    longestWordLength = 0

    for word in words:
        if len(word) > longestWordLength:
            longestWordLength = len(word)
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1

    # get counts by words 
    countsOfWords = {}
    counts = []
    
    for word in wordCounts:
        count = wordCounts[word]
        if count in countsOfWords:
            countsOfWords[count].append(word)
        else:
            countsOfWords[count] = [word]
    
    # sort words alphabetically and an array of counts
    for count in countsOfWords:
        counts.append(count)
        if len(countsOfWords[count]) > 1:
            countsOfWords[count].sort()
    
    # sort counts by value
    counts.sort(reverse=True)

    # print histogram
    spaces = longestWordLength + 2

    for count in counts:
        for word in countsOfWords[count]:
            str = word
            
            # insert spaces
            for i in range(len(word), spaces):
                str = str + " "
            
            # insert hashes for counts
            for i in range(count):
                str = str + "#"
            
            print(str)

    

      
