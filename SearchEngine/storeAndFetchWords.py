#The problems in this chapter are all related to search engine functionality, specifically word searching, storage handling,
#and document fetching. Some of these features will include autocomplete functionality, checks to see if a query can be broken
#up into multiple words, and search result ranking and organization.

#1: Store and Fetch Words
#1. Design a system for storing and fetching words with efficiency - we will use this to make it easier to store web pages for 
#when users are searching our database. We can do this most efficiently by implementing a trie, and giving it methods to insert words,
#search for a word, and search for a prefix.

class Node():
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordList():
    def __init__(self):
        self.root = Node()

    def insertWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children.get(char)
        node.isWord = True

    def searchWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children.get(char)
        return node.isWord

    def searchPrefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children.get(char)
        return True


words = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

myList = WordList()

for word in range(len(words)):
    myList.insertWord(words[word])

print(myList.searchWord("the"))
print(myList.searchPrefix("c"))