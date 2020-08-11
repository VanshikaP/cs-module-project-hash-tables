def no_dups(s):
    # Your code here
    counts = {}

    str = ""
    out = ""

    for char in s:
        if char.isalpha() or char is " ":
            str = str + char.lower()
        
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        elif word != "":
            counts[word] = 1

    for word in counts:
        out = out + word + " "
    
    words2 = list(counts.keys())
    str2 = " ".join(words2)
    print(str2)
    return out.strip()

no_dups("spam spam spam eggs spam sausage spam spam and spam")
# if __name__ == "__main__":
#     print(no_dups(""))
#     print(no_dups("hello"))
#     print(no_dups("hello hello"))
#     print(no_dups("cats dogs fish cats dogs"))
#     print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))