#The problems in this chapter are all related to content displaying functionality, and how it can be optimized - this is obviously a major goal for a 
#content-streaming service like Netflix. Primarily, we’ll focus on problems related to the search and recommendation functionality.

#7 - Browse Ratings:
#In this feature, the user will be able to randomly browse through movie titles and read their summaries and reviews. We want to 
#enable a Back button so the user can return to the previous title in the viewing history. We also want the user to immediately 
#get the title with the highest viewer rating from their viewing history. We want to implement both of these operations in constant 
#time to provide a good user experience. We’ll be provided with a sequential input of ratings to simulate the user viewing them one 
#by one. For simplicity, we’ll assume that the movie ratings are all unique.

from Stack import *

class maxStack:
    def __init__(self):
        self.maxStack = Stack()
        self.mainStack = Stack()
        return
    
    def pop(self):
        if self.mainStack.peek() == self.maxStack.peek():
            self.maxStack.pop()
        return self.mainStack.pop()

    def push(self, value):
        self.mainStack.push(value)
        if (self.maxStack.is_empty() or value > self.maxStack.peek()):
            self.maxStack.push(value)

    def maxRating(self):
        if not self.maxStack.is_empty():
            return self.maxStack.peek()


ratings = maxStack()

ratings.push(3)
ratings.push(4)
ratings.push(1)
ratings.push(0)
ratings.push(6)
ratings.push(14)
ratings.push(2)
ratings.push(10)
ratings.push(35)

print("User navigates through 9 pages and this is the rating history: \n")
ratings.mainStack.print_stack()
ratings.maxStack.print_stack()

print("Current max:  " + str(ratings.maxRating()))

ratings.pop()
ratings.pop()
print("\nUser clicks back button twice:\n")
ratings.mainStack.print_stack()
ratings.maxStack.print_stack()
print("Current max: " + str(ratings.maxRating()))