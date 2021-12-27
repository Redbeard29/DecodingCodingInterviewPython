#Facebook is a huge social media platform, and they own a number of other social media platforms, 
#notably instagram. The majority of the problems in this chapter are related to improving connections between 
#all of Facebook’s platforms, because this will allow users to share and view content across FB’s platforms, 
#improving user experience. 

#5 - Flag Words:
#Facebook recently conducted a survey on the techniques people use to hide offensive or profane words. The goal was to flag such words in the 
#posts and messages of users. The most observable pattern was that the characters of a word were repeated multiple times to avoid detection. 
#A single character in a word was observed to be repeated at least 3 times. This means that characters repeated less than 3 times will be ignored 
#in the detection process. We’ll be provided with a string, S, representing the profane or offensive input word and another string, W, representing 
#the original word. We have to determine if the original word, W, can be modified into S following the above-mentioned rules.


##Naive solution with three separate loops and a frequency counter:

def flag_words(string, dirty_word):
    if string == dirty_word:
        return True

    char_counter = {}

    for char in string:
        char_counter[char] = char_counter.get(char, 0) + 1

    print(char_counter)

    for char in dirty_word:
        if char not in char_counter:
            return False
        else:
            char_counter[char] = char_counter.get(char, 0) - 1
    print(char_counter)

    for key, value in char_counter.items():
        if value < 0 or value == 1:
            return False
    return True

print(flag_words("moooronnnn", "moron"))