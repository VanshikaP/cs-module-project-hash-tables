def word_count(s):
    # Your code here
    counts = {}

    str = ""
    ignoredChars = ["\"", ":", ";", ",", ".", "-", "+" ,"=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]
    
    for char in s:
        if char not in ignoredChars:
            str = str + char.lower()
        
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        elif word != "":
            counts[word] = 1
    
    return counts



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))