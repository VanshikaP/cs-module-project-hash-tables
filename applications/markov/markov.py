import random

# Read in all the words in one go
with open("input.txt") as f:
    text = f.read()
    words = text.split()

    

# TODO: analyze which words can follow other words
# Your code here
wordsTrail = {}

# build the dataset
for i in range(len(words) - 1):
    if words[i] in wordsTrail:
        wordsTrail[words[i]].append(words[i+1])
    else:
        wordsTrail[words[i]] = [words[i+1]]




# get all start words
def isStartWord(word):
    return word[0].isupper() or (word[0] is '"' and word[1].isupper())

startWords = [word for word in words if isStartWord(word)]
# print(startWords)

# get all stop words
def isStopWord(word):
    punctuations = [".", "?", "!"]
    if word[len(word) - 1] in punctuations:
        return True
    if word[len(word) - 1] is '"' and word[len(word)-2] in punctuations:
        return True
    return False

stopWords = [word for word in words if isStopWord(word)]
# print(stopWords)

# TODO: construct 5 random sentences
# Your code here
for i in range(5):
    startWord = random.choice(startWords)
    sentence = ""
    word = startWord
    running = True
    while running:
        sentence = sentence + " " + word
        if word in stopWords:
            running = False
        else:
            word = random.choice(wordsTrail[word])
    
    # Stretch - Closing quote

    quoteCount = 0
    for char in sentence:
        if char is '"':
            quoteCount += 1
    
    if quoteCount % 2 is 1:
        sentence = sentence + '"'
        
    print(sentence.strip())



